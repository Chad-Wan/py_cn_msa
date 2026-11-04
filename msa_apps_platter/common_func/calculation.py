
import math
import numpy as np

def calculate_depth_and_lateral_distance(sonar_data:np.ndarray, attitude_data: list, sound_speed: float):
    pass

def degrees2radians(degrees: float):
    return math.radians(degrees)

def matrix_rotate_x(angle: float):
    a = degrees2radians(angle)
    return np.array([
        [1, 0, 0],
        [0, math.cos(a), -math.sin(a)],
        [0, math.sin(a), math.cos(a)]
    ])

def matrix_rotate_y(angle: float):
    a = degrees2radians(angle)
    return np.array([
        [math.cos(a), 0, math.sin(a)],
        [0, 1, 0],
        [-math.sin(a), 0, math.cos(a)]
    ])

def matrix_rotate_z(angle: float):
    a = degrees2radians(angle)
    return np.array([
        [math.cos(a), -math.sin(a), 0],
        [math.sin(a), math.cos(a), 0],
        [0, 0, 1]
    ])

def delta_enu2new_lonlat(lon: float, lat: float, east: float, north: float):
    R =6371000.0
    lat_rad = math.radians(lat)
    # calculate latitude and longitude
    delta_lat = north / R
    lat_new = lat + math.degrees(delta_lat)

    # calculate latitude and longitude
    r = R * math.cos(lat_rad)
    delta_lon = east / r
    lon_new = lon + math.degrees(delta_lon)

    return lon_new, lat_new


def calculate_multibeam_final_lon_lat_depth(
        two_way_travel_time: float,                # two way travel time
        beam_angle: float,          # beam angle
        sound_speed: float,         # sound speed
        roll_angle: float,          # attitude:: ship roll
        pitch_angle: float,         # attitude:: ship pitch
        heading_angle: float,       # attitude:: ship heading angle
        gps_lon: float,             # longitude
        gps_lat: float,             # latitude
        transductor_draft: float,   # sonar equipment depth under sea
        tide: float):               # sea level

    # 1. calculate slant length:
    slant_length = sound_speed * two_way_travel_time / 2.0

    # 2. calculate reflection point Coordinates(based on ship axis):
    coordinate_ship = np.array([
        [slant_length * math.sin(degrees2radians(beam_angle))],
        [0],
        [-slant_length * math.cos(degrees2radians(beam_angle))]
    ])

    # 3. fix pitch
    coordinate = matrix_rotate_x(pitch_angle) @ coordinate_ship

    # 4. fix roll
    coordinate = matrix_rotate_y(roll_angle) @ coordinate

    # 5. fix heading
    coordinate = matrix_rotate_z(heading_angle) @ coordinate

    # 6. extract to East Longitude and North Latitude
    east, north, up = coordinate.flatten()

    # 7. calculate the real longitude and latitude
    lon_final, lat_final = delta_enu2new_lonlat(gps_lon, gps_lat, east, north)

    # 8. calculate the final depth
    depth_final = - up + transductor_draft - tide

    return lon_final, lat_final, depth_final


def gen_gps_depth_pairs(one_area_sweep: dict, sound_speed: float, transductor_draft: float, tide_file='',
                        pitch_offset_fixed=0.0, roll_offset_fixed=0.0, heading_offset_fixed=0.0):
    area_data = []

    for one_line_sweep in one_area_sweep:

        [pitch_angle, roll_angle, heading_angle] = one_line_sweep["attitude"]
        [gps_lon, gps_lat] = one_line_sweep["gps"]

        # TODO: the tide shall be replaced by a function, because this value is changing when doing the measurement
        tide = 0.0

        # store final lon, lat, depth in the list below
        one_line_data = []

        for one_point in one_line_sweep["data"]:
            [beam_angle, twtt] = one_point

            lon_final, lat_final, depth_final = (
                calculate_multibeam_final_lon_lat_depth(twtt, beam_angle, sound_speed,
                                                        roll_angle + roll_offset_fixed, pitch_angle + pitch_offset_fixed, heading_angle + heading_offset_fixed,
                                                        gps_lon, gps_lat,
                                                        transductor_draft, tide))

            one_line_data.append([lon_final, lat_final, depth_final])

        area_data.append(one_line_data)

    # area_data data frame:
    #     1. line_number is len(area_data), it is unsure due to there may be different number lines inside one area sweep.
    #        the larger the sweep area is, the more the lines will be.
    #     2. each area_data[x] means a independent line sweep.
    #        len(area_data[x])==256. also means 256 points in area_data[x]
    #     3. each area_data[x][y] means a independent point switch.
    #        len(area_data[x][y])==3, there are 3 items inside each area_data: [longitude, latitude, water_depth]
    area_data = np.array(area_data)

    return area_data


def haversine(lat1, lon1, lat2, lon2):
    """已知两点经纬度，求两点间大圆距离（米）"""
    R = 6371000
    phy1, phy2 = math.radians(lat1), math.radians(lat2)
    delta_phy = math.radians(lat2 - lat1)
    delta_lamda = math.radians(lon2 - lon1)
    a = math.sin(delta_phy/2)**2 + math.cos(phy1) * math.cos(phy2) * math.sin(delta_lamda/2)**2
    return 2 * R * math.asin(math.sqrt(a))
