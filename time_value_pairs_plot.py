import matplotlib.pyplot as plt
from datetime import datetime

def make_time_value_pairs(lines: list):
    time_points = []
    values = []
    for line in lines:
        if len(line.split("\t"))==3:
            date_point, time_point, tid = line.split("\t")
            year, month, day = date_point.split("/")
            hour, minute, second = time_point.split(":")

            year = int(year)
            month = int(month)
            day = int(day)
            hour = int(hour)
            minute = int(minute)
            second = int(second)
            tid = float(tid)

            time_points.append(datetime(year, month, day, hour, minute, second))
            values.append(tid)
        else:
            continue

    return time_points, values

file_paths = ["E:\\BZHCL\\2026BZ.tid"]
for file_path in file_paths:
    f = open(file_path, "r")
    lines = f.readlines()
    f.close()

    time_points, values = make_time_value_pairs(lines)

    plt.plot(time_points, values)

plt.show()