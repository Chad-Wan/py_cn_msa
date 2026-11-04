import os
import pyxtf
import numpy as np
import struct

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


