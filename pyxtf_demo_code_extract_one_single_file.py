
import os
import pyxtf
import numpy as np
import basic_functions_pyxtf_multibeam
import basic_functions_calculation
import basic_functions_matplotlib
import matplotlib.pyplot as plt

# some comments of this coding project:
# the multi-beam scan is using a soner to detect the sea bed. during the work：
#   1. sonar transducer transmit a signal as a line, to sea bed. this line contains may points(256 in TJ_0703 project)
#   2. sonar transducer recieve a feedback, then store the data as a line
#   3. the action above is repeated during the whole area scan, until the area scan is done

# so, some defintions inside coding:
#     "area_data":  the data set of one area scan, start by enable sonar transducer, end by disable sonar transducer. one project contains many area_data blocks
#     "line_data":  the data set of one time scan. multi-beam transmit a line(256 points inside) to sea bed one time. one line_data is generated then.
#     "point_data": the data of one point in line_data 
#

file_path = os.path.expanduser("~/data/msa_multibeam_20260731_TJ/xtf_z/1217.xtf")
basic_functions_pyxtf_multibeam.get_xtf_revision(file_path)
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


sound_speed = 1500.0
transductor_draft = 2.1

area_data = basic_functions_calculation.gen_gps_depth_pairs(area_data_full, sound_speed, transductor_draft, roll_offset_fixed=5)
# the data is orgnised as:
#     numpy.ndarray(
#     [
#       [ [lon_final_0, lat_final_0, depth_final_0],  ... [lon_final_256, lat_final_256, depth_final_256] ]  # line 0 points inside
#       [ [lon_final_0, lat_final_0, depth_final_0],  ... [lon_final_256, lat_final_256, depth_final_256] ]  # line 1 points inside
#              ...   ...   ...   ...                ...   ...   ...   ...              ...   ...   ...   ...       
#       [ [lon_final_0, lat_final_0, depth_final_0],  ... [lon_final_256, lat_final_256, depth_final_256] ]  # line xx points inside
#     ])


# print(area_data[:,:,2])



