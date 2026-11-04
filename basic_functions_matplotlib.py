import matplotlib.pyplot as plt
import numpy as np


def pyplot_feedback_colormap_value(current_value: float, min_value: float, max_value: float):
    if current_value < min_value:
        return 0.0
    elif current_value > max_value:
        return 1.0
    else:
        return (current_value - min_value) / (max_value - min_value)



# usage: 
# for i in range(len(x)):
#     plt.scatter(x[i],y[i],c=pyplot_feedback_rainbow_color(y[i], 0, 20))
def pyplot_feedback_rainbow_color(current_value: float, min_value: float, max_value: float):
    color_value = pyplot_feedback_colormap_value(current_value, min_value, max_value)
    cm = plt.cm.rainbow(color_value)
    return cm



def pyplot_draw_3d_plot(ax, points: list, min_value=0, max_value=35):
     # points structure:
     # [
     #   [x0, y0, z0],
     #   [x1, y1, z1],
     #     ...  ...
     #   [xn, yn, zn]
     # ]
     for point in points:
         ax.scatter(point[0], point[1], point[2], color=pyplot_feedback_rainbow_color(point[2], min_value, max_value), s=1)
