import basic_functions_pyxtf_multibeam
import pyproj
import os
import pandas as pd
import openpyxl
from openpyxl.styles import Alignment, Font

def angle_to_arrow(angle):
    """把角度归一化到 0~360 后映射到箭头。
    非 45° 倍数的角度会报错，方便你发现脏数据。"""
    # 归一化：支持负数和超过 360 的值
    a = round(float(angle)) % 360
    if a not in ARROW_MAP:
        raise ValueError(f"角度 {angle}° 不是 45° 的倍数")
    return ARROW_MAP[a]

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

def get_all_files_in_dir(folder_path: str):
    folder_path = os.path.expanduser(folder_path)
    files = []
    items = os.listdir(folder_path)
    # print(items)
    for item in items:
        if os.path.isfile(folder_path + item) and "xtf" in item:
            files.append(folder_path + item)
    return sorted(files)

def format_time(time_list: list):
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i])
    date = "-".join(time_list[0:3])
    time_point = ":".join(time_list[3:])
    return date + " " + time_point

def get_single_multibeam_scan_recording(xtf_file_path: str):
    xtf_file_header, packets = basic_functions_pyxtf_multibeam.get_file_header_and_packets(xtf_file_path)
    sonar_data = basic_functions_pyxtf_multibeam.extract_packet_multibeam_data(packets)

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

    return [file_name, time_start, time_end, dist, az12, generate_new_approximate_angle(az12)]

# xtf_file_path = os.path.expanduser("~/data/msa_multibeam_20260731_TJ/xtf_z/")
xtf_file_path = os.path.expanduser("/home/wan/data/BinZhou_Port_2026/Export/2356 - Noname - 0001.xtf")
# xtf_file_path = os.path.expanduser("/home/wan/data/BinZhou_Port_2026/0923/xtf/")
# xtf_file_path = "/home/wan/data/BinZhou_Port_2026/0923/db/"

get_single_multibeam_scan_recording(xtf_file_path)