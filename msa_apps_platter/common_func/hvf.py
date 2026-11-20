
import xmltodict
import os
from common_func.basic_func import find_all_subfiles_with_certain_patterns
from field_collection_record_sheet import field_collection_recording_export_ui
from common_func.pyxtf_multibeam import get_single_multibeam_scan_recording
from datetime import date, datetime, timedelta
import pandas as pd


def date_to_doy(year: int, month: int, day: int):
    dt = date(year, month, day)
    return dt.timetuple().tm_yday

# 字符串日期（例“2026-10-12”）转换成累计时间（例“2026-285”）
def str_date_to_str_doy(str_date: str):
    [year, month, day] = str_date.split("-")
    year = int(year)
    month = int(month)
    day = int(day)

    doy = date_to_doy(year, month, day)

    return str(year) + "-" + str(doy)

# 字符串日期时间（例“2026-10-12 12:13:14”）转换成累计时间（例“2026-285 12:13:14”）
def str_datetime_to_str_doytime(str_datetime: str):
    str_date = str_datetime.split("T")[0]
    str_time = str_datetime.split("T")[1].split(".")[0]
    # str_date = str_date_to_str_doy(str_date)
    # print(str_date)
    return str_date_to_str_doy(str_date) + " " + str_time


def doy_to_date(year: int, doy: int, hour:int, minute: int, second: int):
    dt = datetime(year, 1, 1, hour, minute, second)
    res = dt + timedelta(days=doy - 1)
    return res


# 将data里面的全部内容写进hvf文件，hvf的路径和文件名又file_path决定
def write_hml(file_path: str, data: dict):
    file_path = os.path.abspath(os.path.expanduser(file_path))
    with open(file_path, "w", encoding="utf-8") as f:
        xmltodict.unparse(data, f, pretty=True)

# 读取hvf文件里面的全部内容，返回值为一个字典。hvf文件地址由file_path
def read_hml(file_path: str):
    file_path = os.path.abspath(os.path.expanduser(file_path))
    with open(file_path) as f:
        data = xmltodict.parse(f.read())
    return data

# 根据提供的date,X,Y,Z,pitch,roll,yaw, 生成一个字典，这个字典可以作为最小数据元放在DepthSensor下面
# 添加在data中，这个data后期会直接写进hvf文件
def generate_one_hvf_item_depth(date_time: str, X: str, Y: str, Z: str, pitch: str, roll: str, yaw: str):
    new_item = {
        '@value': date_time, # '2026-149 06:18:00'
        'Latency':
            {
                '@value': '0.000000'
            },
        'SensorClass':
            {
                '@value': 'Swath'
            },
        'TransducerEntries':
            {
                'Transducer':
                    {
                        '@Number': '1',
                        '@StartBeam': '1',
                        '@Model': 'Unknown',
                        'Offsets':
                            {
                                '@X': X,            # '0.000000',
                                '@Y': Y,            # '0.000000',
                                '@Z': Z,            # '1.950000',
                                '@Latency': '0.000000'
                            },
                        'MountAngle':
                            {
                                '@Pitch': pitch,    # '-5.700000',
                                '@Roll': roll,      # '0.880000',
                                '@Azimuth': yaw     # '-1.000000'
                            }
                    }
            }
    }
    return new_item

def generate_one_hvf_item_svp(date_time: str, DualHead: str, X: str, Y: str, Z: str, pitch: str, roll: str, yaw: str,
                               X2='0.0', Y2='0.0', Z2='0.0', pitch2='0.0', roll2='0.0', yaw2='0.0'):
    if DualHead == "Yes":
        new_item = {
            '@value': date_time,
            'Latency': {
                '@value': '0.000000'
            },
            'DualHead': {
                '@value': 'Yes'
            },
            'Offsets': {
                '@X': X,
                '@Y': Y,
                '@Z': Z,
                '@X2': X2,
                '@Y2': Y2,
                '@Z2': Z2
            },
            'MountAngle': {
                '@Pitch': pitch,
                '@Roll': roll,
                '@Azimuth': yaw,
                '@Pitch2': pitch2,
                '@Roll2': roll2,
                '@Azimuth2': yaw2
            }
        }
    else:
        new_item = {
            '@value': date_time,
            'Latency': {
                '@value': '0.000000'
            },
            'DualHead': {
                '@value': 'No'
            },
            'Offsets': {
                '@X': X,
                '@Y': Y,
                '@Z': Z
            },
            'MountAngle': {
                '@Pitch': pitch,
                '@Roll': roll,
                '@Azimuth': yaw
            }
        }

    return new_item

def get_score(item):
    return item["date_time"]

# TODO
def read_interested_hvf_items_svp_sensor(data: dict):
    set_list = []
    for item in data['HIPSVesselConfig']['SVPSensor']['TimeStamp']:
        # print(item)
        date_time = item['@value']
        dual_head = item['DualHead']['@value']
        X = item['Offsets']['@X']
        Y = item['Offsets']['@Y']
        Z = item['Offsets']['@Z']
        pitch = item['MountAngle']['@Pitch']
        roll = item['MountAngle']['@Roll']
        yaw = item['MountAngle']['@Azimuth']

        if dual_head == "Yes":
            X2 = item['Offsets']['@X2']
            Y2 = item['Offsets']['@Y2']
            Z2 = item['Offsets']['@Z2']
            pitch2 = item['MountAngle']['@Pitch2']
            roll2 = item['MountAngle']['@Roll2']
            yaw2 = item['MountAngle']['@Azimuth2']
            dict_temp = {
                "date_time" : date_time,
                "dual_head": dual_head,
                "X" : X,
                "Y" : Y,
                "Z" : Z,
                "pitch" : pitch,
                "roll" : roll,
                "yaw" : yaw,
                "X2": X2,
                "Y2": Y2,
                "Z2": Z2,
                "pitch2": pitch2,
                "roll2": roll2,
                "yaw2": yaw2
            }
            set_list.append(dict_temp)
        elif dual_head == "No":
            dict_temp = {
                "date_time": date_time,
                "dual_head": dual_head,
                "X": X,
                "Y": Y,
                "Z": Z,
                "pitch": pitch,
                "roll": roll,
                "yaw": yaw,
                "X2": '0.0',
                "Y2": '0.0',
                "Z2": '0.0',
                "pitch2": '0.0',
                "roll2": '0.0',
                "yaw2": '0.0'
            }
            set_list.append(dict_temp)
        else:
            print("ERROR:: dual_head value error!! @ read_interested_hvf_items_svp_sensor")
    set_list.sort(key=get_score)

    set_list_formatted = []
    for setting in set_list:
        date_time = setting['date_time'].split(" ")
        year = int(date_time[0].split("-")[0])
        doy = int(date_time[0].split("-")[1])
        hour = int(date_time[1].split(":")[0])
        minute = int(date_time[1].split(":")[1])
        second = int(date_time[1].split(":")[2])
        date_time = doy_to_date(year, doy, hour, minute, second)

        setting['date_time'] = date_time
        dual_head = setting['dual_head']
        setting['X'] = float(setting['X'])
        setting['Y'] = float(setting['Y'])
        setting['Z'] = float(setting['Z'])
        setting['pitch'] = float(setting['pitch'])
        setting['roll'] = float(setting['roll'])
        setting['yaw'] = float(setting['yaw'])

        if dual_head == "Yes":
            setting['X2'] = float(setting['X2'])
            setting['Y2'] = float(setting['Y2'])
            setting['Z2'] = float(setting['Z2'])
            setting['pitch2'] = float(setting['pitch2'])
            setting['roll2'] = float(setting['roll2'])
            setting['yaw2'] = float(setting['yaw2'])
        elif dual_head == "No":
            setting['X2'] = 0.0
            setting['Y2'] = 0.0
            setting['Z2'] = 0.0
            setting['pitch2'] = 0.0
            setting['roll2'] = 0.0
            setting['yaw2'] = 0.0
        else:
            print("ERROR:: dual_head value error!! @ read_interested_hvf_items_svp_sensor")

        set_list_formatted.append(setting)

    # [
    # {'date_time': datetime.datetime(2026, 4, 21, 0, 0), 'X': 0.0, 'Y': 0.0, 'Z': 1.67, 'pitch': 4.0, 'roll': 1.89, 'yaw': 5.0, 'X2': 0.0, 'Y2': 0.0, 'Z2': 1.67, 'pitch2': 4.0, 'roll2': 1.89, 'yaw2': 5.0 },
    #     ....   ....   ....
    # {'date_time': datetime.datetime(2026, 6, 2, 0, 0), 'X': 0.0, 'Y': 0.0, 'Z': 1.96, 'pitch': -5.7, 'roll': 0.78, 'yaw': -1.0, 'X2': 0.0, 'Y2': 0.0, 'Z2': 1.67, 'pitch2': 4.0, 'roll2': 1.89, 'yaw2': 5.0}
    # ]
    return set_list_formatted

# 分析下生成的data文件，把感兴趣的hvf部分提取出来，并简化成一个list
def read_interested_hvf_items_depth_sensor(data: dict):
    set_list = []
    for item in data['HIPSVesselConfig']['DepthSensor']['TimeStamp']:
        date_time = item['@value']
        X = item['TransducerEntries']['Transducer']['Offsets']['@X']
        Y = item['TransducerEntries']['Transducer']['Offsets']['@Y']
        Z = item['TransducerEntries']['Transducer']['Offsets']['@Z']
        pitch = item['TransducerEntries']['Transducer']['MountAngle']['@Pitch']
        roll = item['TransducerEntries']['Transducer']['MountAngle']['@Roll']
        yaw = item['TransducerEntries']['Transducer']['MountAngle']['@Azimuth']
        dict_temp = {
            "date_time": date_time,
            "X": X,
            "Y": Y,
            "Z": Z,
            "pitch": pitch,
            "roll": roll,
            "yaw": yaw
        }
        set_list.append(dict_temp)
    set_list.sort(key=get_score)

    set_list_formatted = []
    for setting in set_list:
        date_time = setting['date_time'].split(" ")
        year = int(date_time[0].split("-")[0])
        doy = int(date_time[0].split("-")[1])
        hour = int(date_time[1].split(":")[0])
        minute = int(date_time[1].split(":")[1])
        second = int(date_time[1].split(":")[2])
        date_time = doy_to_date(year, doy, hour, minute, second)
        setting['date_time'] = date_time

        setting['X'] = float(setting['X'])
        setting['Y'] = float(setting['Y'])
        setting['Z'] = float(setting['Z'])
        setting['pitch'] = float(setting['pitch'])
        setting['roll'] = float(setting['roll'])
        setting['yaw'] = float(setting['yaw'])

        set_list_formatted.append(setting)

    # [
    # {'date_time': datetime.datetime(2026, 4, 21, 0, 0), 'X': 0.0, 'Y': 0.0, 'Z': 1.67, 'pitch': 4.0, 'roll': 1.89, 'yaw': 5.0},
    #     ....   ....   ....
    # {'date_time': datetime.datetime(2026, 6, 2, 0, 0), 'X': 0.0, 'Y': 0.0, 'Z': 1.96, 'pitch': -5.7, 'roll': 0.78, 'yaw': -1.0}
    # ]
    return set_list_formatted


def get_test_line_info_from_xtf_files(folder_path:str):
    test_line_info = []
    files = find_all_subfiles_with_certain_patterns(folder_path, ".xtf")
    for file in files:
        print(file + "   ----> processing done")
        [file_name, time_start, time_end, dist, az12, az12] = get_single_multibeam_scan_recording(file)
        file_name = str(file_name).replace("b'","").replace("'","")
        date_time = time_start.split(" ")
        year = int(date_time[0].split("-")[0])
        month = int(date_time[0].split("-")[1])
        day = int(date_time[0].split("-")[2])
        hour = int(date_time[1].split(":")[0])
        minute = int(date_time[1].split(":")[1])
        second = int(date_time[1].split(":")[2])
        time_start = datetime(year, month, day, hour, minute, second)
        date_time = time_end.split(" ")
        year = int(date_time[0].split("-")[0])
        month = int(date_time[0].split("-")[1])
        day = int(date_time[0].split("-")[2])
        hour = int(date_time[1].split(":")[0])
        minute = int(date_time[1].split(":")[1])
        second = int(date_time[1].split(":")[2])
        time_end = datetime(year, month, day, hour, minute, second)
        test_line_info.append({
            'file_name':file_name,
            'start_time':time_start,
            'end_time':time_end,
            'X': 0.0,
            'Y': 0.0,
            'Z': 0.0,
            'pitch': 0.0,
            'roll': 0.0,
            'yaw': 0.0,
            'direction': az12
        })
    # 输出格式
    # [
    #   {'file_name': b'1234 - Noname - 0001.xtf', 'start_time': '2026-7-30 8:8:48', 'end_time': '2026-7-30 8:11:1' ...}
    #      ....   ....   ....
    #   {'file_name': b'1244 - Noname - 0001.xtf', 'start_time': '2026-7-30 8:49:11', 'end_time': '2026-7-30 8:49:56' ...}
    # ]
    return pd.DataFrame(test_line_info)






def reorder_the_hvf_existing_settings_transducer(hvf_file_path:str, xtf_dataframe:pd.DataFrame):
    # 解析全部hvf文件信息
    data = read_hml(hvf_file_path)
    # 读取现有测线信息
    set_list = read_interested_hvf_items_depth_sensor(data)
    # print(len(set_list))
    # print(set_list)
    # 读取原始xtf数据的文件名和运行时间
    # xtf_dataframe = get_test_line_info_from_xtf_files(xtf_file_folder_path)
    # print(xtf_dataframe)

    # xtf_dataframe["threshold_time"] = datetime(1989,1,1,1,1,1)
    # print(xtf_dataframe)

    xtf_dataframe['threshold_time'] = xtf_dataframe["start_time"] + (xtf_dataframe["end_time"] - xtf_dataframe["start_time"]) / 2
    # print(xtf_dataframe.loc[:,["file_name", 'threshold_time']])

    xtf_dataframe['matched_setting_number'] = 99
    temp = 0

    count = 0

    for i in range(len(set_list)):
        for j in range(xtf_dataframe.shape[0]):
            a = set_list[i]['date_time']
            b = xtf_dataframe.loc[j, 'threshold_time'].to_pydatetime()

            if j == 0:
                if a < xtf_dataframe.loc[0, 'threshold_time'].to_pydatetime():
                    xtf_dataframe.loc[j, "matched_setting_number"] = 0
                continue

            if j>=1:
                state = (a < xtf_dataframe.loc[j, 'threshold_time'].to_pydatetime()) and (a > xtf_dataframe.loc[j - 1, 'threshold_time'].to_pydatetime())
                if state:
                    pass

            if (a < xtf_dataframe.loc[j, 'threshold_time'].to_pydatetime()) and (a > xtf_dataframe.loc[j-1, 'threshold_time'].to_pydatetime()):
                xtf_dataframe.loc[j, "matched_setting_number"] = i
                temp = i
            elif a < xtf_dataframe.loc[j, 'threshold_time'].to_pydatetime():
                xtf_dataframe.loc[j, "matched_setting_number"] = temp
            else:
                pass
                # xtf_dataframe.loc[j, "matched_setting_number"] = temp

    # 对于已经有的配置，逐条归档到xtf dataframe里面
    for i in range(len(xtf_dataframe)):
        xtf_dataframe.loc[i, 'X'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["X"]
        xtf_dataframe.loc[i, 'Y'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["Y"]
        xtf_dataframe.loc[i, 'Z'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["Z"]
        xtf_dataframe.loc[i, 'pitch'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["pitch"]
        xtf_dataframe.loc[i, 'roll'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["roll"]
        xtf_dataframe.loc[i, 'yaw'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["yaw"]

    # print(set_list)

    return xtf_dataframe.loc[:, ["file_name", "start_time", "end_time", 'X', 'Y', 'Z', 'pitch', 'roll', 'yaw', 'direction']]


def reorder_the_hvf_existing_settings_svp_sensor(hvf_file_path:str, xtf_dataframe:pd.DataFrame):
    # 解析全部hvf文件信息
    data = read_hml(hvf_file_path)
    # 读取现有测线信息
    set_list = read_interested_hvf_items_svp_sensor(data)
    # print(len(set_list))
    # print(set_list)
    # 读取原始xtf数据的文件名和运行时间
    # xtf_dataframe = get_test_line_info_from_xtf_files(xtf_file_folder_path)
    # print(xtf_dataframe)

    # xtf_dataframe["threshold_time"] = datetime(1989,1,1,1,1,1)
    # print(xtf_dataframe)

    xtf_dataframe['threshold_time'] = xtf_dataframe["start_time"] + (xtf_dataframe["end_time"] - xtf_dataframe["start_time"]) / 2
    # print(xtf_dataframe.loc[:,["file_name", 'threshold_time']])

    xtf_dataframe['matched_setting_number'] = 99
    xtf_dataframe['DualHead'] = "Yes"
    temp = 0

    count = 0

    for i in range(len(set_list)):
        for j in range(xtf_dataframe.shape[0]):
            a = set_list[i]['date_time']
            b = xtf_dataframe.loc[j, 'threshold_time'].to_pydatetime()

            if j == 0:
                if a < xtf_dataframe.loc[0, 'threshold_time'].to_pydatetime():
                    xtf_dataframe.loc[j, "matched_setting_number"] = 0
                continue

            if j>=1:
                state = (a < xtf_dataframe.loc[j, 'threshold_time'].to_pydatetime()) and (a > xtf_dataframe.loc[j - 1, 'threshold_time'].to_pydatetime())
                if state:
                    pass

            if (a < xtf_dataframe.loc[j, 'threshold_time'].to_pydatetime()) and (a > xtf_dataframe.loc[j-1, 'threshold_time'].to_pydatetime()):
                xtf_dataframe.loc[j, "matched_setting_number"] = i
                temp = i
            elif a < xtf_dataframe.loc[j, 'threshold_time'].to_pydatetime():
                xtf_dataframe.loc[j, "matched_setting_number"] = temp
            else:
                pass
                # xtf_dataframe.loc[j, "matched_setting_number"] = temp

    # 对于已经有的配置，逐条归档到xtf dataframe里面
    for i in range(len(xtf_dataframe)):
        # print(set_list)
        xtf_dataframe.loc[i, 'DualHead'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["dual_head"]

        xtf_dataframe.loc[i, 'X'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["X"]
        xtf_dataframe.loc[i, 'Y'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["Y"]
        xtf_dataframe.loc[i, 'Z'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["Z"]
        xtf_dataframe.loc[i, 'pitch'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["pitch"]
        xtf_dataframe.loc[i, 'roll'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["roll"]
        xtf_dataframe.loc[i, 'yaw'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["yaw"]

        xtf_dataframe.loc[i, 'X2'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["X2"]
        xtf_dataframe.loc[i, 'Y2'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["Y2"]
        xtf_dataframe.loc[i, 'Z2'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["Z2"]
        xtf_dataframe.loc[i, 'pitch2'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["pitch2"]
        xtf_dataframe.loc[i, 'roll2'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["roll2"]
        xtf_dataframe.loc[i, 'yaw2'] = set_list[xtf_dataframe.loc[i, "matched_setting_number"]]["yaw2"]



    # print(set_list)

    return xtf_dataframe.loc[:, ["file_name", "start_time", "end_time", 'DualHead', 'X', 'Y', 'Z', 'pitch', 'roll', 'yaw', 'X2', 'Y2', 'Z2', 'pitch2', 'roll2', 'yaw2', 'direction']]


def reorder_the_hvf_existing_settings(hvf_file_path: str, xtf_file_folder_path: str):
    xtf_dataframe_depth = get_test_line_info_from_xtf_files(xtf_file_folder_path)
    xtf_dataframe_svp = xtf_dataframe_depth.copy()

    depth_dataframe = reorder_the_hvf_existing_settings_transducer(hvf_file_path, xtf_dataframe_depth)
    svp_dataframe = reorder_the_hvf_existing_settings_svp_sensor(hvf_file_path, xtf_dataframe_svp)

    return depth_dataframe, svp_dataframe


# print(date_to_doy(2026, 10, 8))


# # #
# hvf_file_path = "/home/wan/data/hvf_file_demo/2026wxm.hvf"
# xtf_folder_path = "/home/wan/data/BinZhou_Port_2026/Export_test"
# xtf_folder_path = "/home/wan/data/BinZhou_Port_2026/Export"
# data = read_hml(hvf_file_path)
# # # print(read_interested_hvf_items(data))
# # # print(len(read_interested_hvf_items(data)))
# # # print(get_test_line_info_from_xtf_files(xtf_folder_path))
# # print(list(reorder_the_hvf_existing_settings_v2(hvf_file_path, xtf_folder_path)))
# # 显示所有行
# pd.set_option('display.max_rows', None)
# # 显示所有列
# pd.set_option('display.max_columns', None)
# print(reorder_the_hvf_existing_settings_v2(hvf_file_path, xtf_folder_path))
# #
# #
# #
# # # print(data['HIPSVesselConfig']['DepthSensor']['TimeStamp'][-3:-1])
# # #
# # # print(data['HIPSVesselConfig']['DepthSensor'].keys())
# # #
# # # print(data['HIPSVesselConfig'].keys())

# print(data['HIPSVesselConfig']['SVPSensor']['TimeStamp'][0])

# print(reorder_the_hvf_existing_settings(hvf_file_path, xtf_folder_path))
#
# depth_df, svp_df = reorder_the_hvf_existing_settings(hvf_file_path, xtf_folder_path)
# print(depth_df.columns)
# pd.set_option('display.max_rows', None)      # 显示全部行
# pd.set_option('display.max_columns', None)   # 显示全部列
# pd.set_option('display.width', None)         # 自动适配宽度，不折行截断
# print(depth_df)
# print(svp_df)
# print(svp_df['DualHead'])
