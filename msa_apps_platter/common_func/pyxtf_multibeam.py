import os
import pyxtf
import numpy as np
import struct
import pyproj

from pyxtf import XTFHeaderType


# function name: get_file_header_and_packets()
# input:
#   xtf_file_path --> xtf file path, type==srt
# output:
#   file_header --> type==pyxtf.xtf_ctypes.XTFHeaderType
#   packets     --> type==dict
# function description:
#   read the given xtf file, return the file header and packets

def get_file_header_and_packets(xtf_file_path: str):
    file_header, packets = pyxtf.xtf_read(os.path.expanduser(xtf_file_path))
#    print(packets[XTFHeaderType.qinsy_r2sonic_bathy][0].data)
    return file_header, packets



# function name: extract_packet_multibeam_data()
# input:
#   packets --> xtf file packets, type==dict
# output:
#   sonar_data      --> type==numpy.array
#   gps_data        --> type==list
#   attitude_data   --> type==list
#   time_data       --> type==list
# function description:
#   extract the packet data, to get sonar_data,gps_data, attitude_data and time_data

def extract_packet_multibeam_data(packets: dict):
    sonar_data = []

    slices_orig = packets[pyxtf.XTFHeaderType.q_multibeam]

    for slice_orig in slices_orig:
        one_line_data = []
        x_coordinate = slice_orig.SensorXcoordinate
        y_coordinate = slice_orig.SensorYcoordinate
        ship_gyro = slice_orig.ShipGyro
        sensor_roll = slice_orig.SensorRoll
        sensor_pitch = slice_orig.SensorPitch
        year = slice_orig.Year
        month = slice_orig.Month
        day = slice_orig.Day
        hour = slice_orig.Hour
        minute = slice_orig.Minute
        second = slice_orig.Second
        for one_line_sweep in slice_orig.data:
            beam_angle = one_line_sweep.BeamAngle
            two_way_travel_time = one_line_sweep.TwoWayTravelTime
            one_line_data.append([beam_angle, two_way_travel_time])

        gps_data = [x_coordinate, y_coordinate]
        attitude_data = [sensor_pitch, sensor_roll, ship_gyro]
        time_data = [year, month, day, hour, minute, second]
        #
        # print(one_line_data)
        # print(np.array(one_line_data).transpose().shape)

        sonar_data.append({"gps": gps_data,
                           "attitude": attitude_data,
                           "time": time_data,
                           "data": np.array(one_line_data)})

    # output the related data as a list. each list item is a dictionary, containing gps, attitude, time and data
    # all these data are extracted directly from xtf file, without any data process
    return sonar_data


def get_xtf_revision(filepath):
    with open(filepath, 'rb') as f:
        magic, version = struct.unpack('<HH', f.read(4))
    if magic != 0xFACE:
        raise ValueError("不是有效的XTF文件")
    print(f"XTF Version (Rev): {version}")
    return version


def format_time(time_list: list):
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i])
    date = "-".join(time_list[0:3])
    time_point = ":".join(time_list[3:])
    return date + " " + time_point


def generate_new_approximate_angle(old_angle: float):
    if old_angle < 22.5:
        new_angle = 0
    elif 22.5 <= old_angle < 67.5:
        new_angle = 45
    elif 67.5 <= old_angle < 112.5:
        new_angle = 90
    elif 112.5 <= old_angle < 157.5:
        new_angle = 135
    elif 157.5 <= old_angle < 202.5:
        new_angle = 180
    elif 202.5 <= old_angle < 247.5:
        new_angle = 225
    elif 247.5 <= old_angle < 292.5:
        new_angle = 270
    elif 292.5 <= old_angle < 337.5:
        new_angle = 315
    else:
        new_angle = 0
    return new_angle


def get_single_multibeam_scan_recording(xtf_file_path: str):
    xtf_file_header, packets = get_file_header_and_packets(xtf_file_path)
    sonar_data = extract_packet_multibeam_data(packets)

    gps_start = sonar_data[0]["gps"]
    gps_end = sonar_data[-1]["gps"]
    # print(sonar_data[-1].keys())
    # print(gps_start, gps_end)

    # 计算大地方位角，从gps_start到gps_end
    geod = pyproj.Geod(ellps="WGS84")
    # 计算大地方位角
    az12, az21, dist = geod.inv(gps_start[0], gps_start[1], gps_end[0], gps_end[1])
    # 方位角取正数
    if az12 < 0:
        az12 = az12 + 360

    time_start = format_time(sonar_data[0]["time"])
    time_end = format_time(sonar_data[-1]["time"])

    file_name = xtf_file_header.ThisFileName

    return [file_name, time_start, time_end, dist, az12, az12]
