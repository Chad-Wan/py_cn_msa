
import os
import pyxtf
import numpy as np
import basic_functions_pyxtf_multibeam
import basic_functions_calculation
import basic_functions_matplotlib
import basic_functions_visualizition
import basic_functions_filter_algorithm
import pyvista as pv

# some comments of this coding project:
# the multi-beam scan is using a soner to detect the sea bed. during the work：
#   1. sonar transducer transmit a signal as a line, to sea bed. this line contains may points(256 in TJ_0703 project)
#   2. sonar transducer receive a feedback, then store the data as a line
#   3. the action above is repeated during the whole area scan, until the area scan is done

# so, some definitions inside coding:
#     "area_data":  the data set of one area scan, start by enable sonar transducer, end by disable sonar transducer. one project contains many area_data blocks
#     "line_data":  the data set of one time scan. multi-beam transmit a line(256 points inside) to sea bed one time. one line_data is generated then.
#     "point_data": the data of one point in line_data 
#

def read_single_xtf_file(file_path: str, sound_speed: float, transductor_draft: float, tide_file='',
                     pitch_offset_fixed=0.0, roll_offset_fixed=0.0, heading_offset_fixed=0.0):
    # read xtf file
    file_header, packets = basic_functions_pyxtf_multibeam.get_file_header_and_packets(file_path)

    # extract all the points information.
    area_data_full = basic_functions_pyxtf_multibeam.extract_packet_multibeam_data(packets)
    # the area_data_full is a list. all the line data is inside as an element. each line data is orgnised as:
    #    {
    #       "gps": gps_data, 
    #       "attitude": attitude_data,
    #       "time": time_data,
    #       "data": np.array(one_line_data)
    #     }
    #
    # in which:
    #    gps_data = [x_coordinate, y_coordinate]
    #    attitude_data = [sensor_pitch, sensor_roll, ship_gyro]
    #    time_data = [year, month, day, hour, minute, second]
    #    one_line_data is a list of list, is orgnised as [ 
    #                                                      [beam_angle_0, two_way_travel_time_0], 
    #                                                      [beam_angle_1, two_way_travel_time_1],
    #                                                       ... ...    ... ...    ... ...    
    #                                                      [beam_angle_256, two_way_travel_time_256]
    #                                                    ]

    area_data = basic_functions_calculation.gen_gps_depth_pairs(area_data_full, sound_speed, transductor_draft, tide_file=tide_file,
                                                                pitch_offset_fixed=pitch_offset_fixed, roll_offset_fixed=roll_offset_fixed, heading_offset_fixed=heading_offset_fixed)
    # the data is orgnised as:
    #     numpy.ndarray(
    #     [
    #       [ [lon_final_0, lat_final_0, depth_final_0],  ... [lon_final_256, lat_final_256, depth_final_256] ]  # line 0 points inside
    #       [ [lon_final_0, lat_final_0, depth_final_0],  ... [lon_final_256, lat_final_256, depth_final_256] ]  # line 1 points inside
    #              ...   ...   ...   ...                ...   ...   ...   ...              ...   ...   ...   ...       
    #       [ [lon_final_0, lat_final_0, depth_final_0],  ... [lon_final_256, lat_final_256, depth_final_256] ]  # line xx points inside
    #     ])

    return area_data


def read_all_xtf_files(file_folder:str, sound_speed:float, transductor_draft:float, tide_file='',
                       pitch_offset_fixed=0.0, roll_offset_fixed=0.0, heading_offset_fixed=0.0):
    file_path_folder = os.path.expanduser(file_folder)
    file_paths = []
    for file_name in os.listdir(file_path_folder):
        file_path = file_path_folder + file_name
        if os.path.isfile(file_path):
            file_paths.append(file_path)

    # extract all the sonar data, stored in:
    all_sonar_data = []

    for file_path in file_paths:
        area_data = read_single_xtf_file(file_path, sound_speed=sound_speed, transductor_draft=transductor_draft,tide_file=tide_file,
                                         pitch_offset_fixed=pitch_offset_fixed, roll_offset_fixed=roll_offset_fixed, heading_offset_fixed=heading_offset_fixed)
        if len(all_sonar_data)==0:
            all_sonar_data = area_data
        else:
            all_sonar_data = np.concatenate((all_sonar_data, area_data), axis=0)
        print(file_path, ": extract done")

    print("sonar data shape: ", all_sonar_data.shape)
    return all_sonar_data





file_folder = os.path.expanduser("~/data/msa_multibeam_20260731_TJ/xtf_z/")
sound_speed = 1500.0
transductor_draft = 2.1
tide_file = ''
pitch_offset_fixed = 0.0
roll_offset_fixed = 0.0
heading_offset_fixed = 0.0


# =================================
#     formal code: extract all xtf files
# =================================

# all_sonar_data is a 3d array.
# shape = (50000+, 256, 3): 5000+ is sweep line number
# all_sonar_data = read_all_xtf_files(file_folder=file_folder, sound_speed=sound_speed, transductor_draft=transductor_draft, tide_file=tide_file,
#                                     pitch_offset_fixed=0.0, roll_offset_fixed=0.0, heading_offset_fixed=0.0)

# =================================
#     code only for test, extract only one xtf file
# =================================
all_sonar_data = read_single_xtf_file(os.path.expanduser("~/data/msa_multibeam_20260731_TJ/xtf_z/1235.xtf"),
                                      sound_speed=1531.0, transductor_draft=2.1, tide_file='',
                                      pitch_offset_fixed=0.0, roll_offset_fixed=5.0, heading_offset_fixed=0.0)

# decrease to 2D structure，keep the last dimension unchanged.
# all_sonar_data = all_sonar_data[:,:,:].reshape(-1, all_sonar_data.shape[-1])
# all_sonar_data = all_sonar_data[:,:,:].reshape(-1, all_sonar_data.shape[-1]).astype(np.float32)
# =================================
#     filter code area:
#  all_sonar_data is the original points, which come form raw xtf files
#  all_sonar_data_processed is the processed points by algorithm.
# =================================
all_sonar_data_processed = np.array(
    [0.0, 0.0, 0.0]
)

deal_together = 3
for i in range(len(all_sonar_data)-deal_together-1):
    # tmp, status = basic_functions_filter_algorithm.shallow_water_sor_filter(all_sonar_data[i:i+deal_together-1])
    tmp, status = basic_functions_filter_algorithm.shallow_water_sor_filter(all_sonar_data[i])
    tmp, status, _ = basic_functions_filter_algorithm.remove_islands_connected_components(tmp)
    # tmp, status = basic_functions_filter_algorithm.traditional_sor_filter(line)
    all_sonar_data_processed = np.vstack((all_sonar_data_processed, tmp))


# =================================
#  plot the raw data and processed data in one picture
# =================================

all_sonar_data = all_sonar_data[:,:,:].reshape(-1, all_sonar_data.shape[-1])
basic_functions_visualizition.plot_dual_point_cloud(all_sonar_data, all_sonar_data_processed)
