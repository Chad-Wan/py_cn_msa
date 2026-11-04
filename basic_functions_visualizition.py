
import numpy as np
import pyvista as pv


def plot_dual_point_cloud(point_sets_original: np.ndarray,
                          point_sets_processed: np.ndarray):
    # 构造 PolyData（VTK 共享内存，不拷贝）
    pc_orig = pv.PolyData(point_sets_original)
    pc_processed = pv.PolyData(point_sets_processed)

    # 可选：加一个标量用于上色（比如高度）
    pc_orig.point_data["z"] = point_sets_original[:, 2]
    pc_processed.point_data["z"] = point_sets_processed[:, 2]


    # visualiztion, the original signal is on the left; the processed one is on the right 
    pl = pv.Plotter(shape=(1, 2))

    # ==================================================
    # plot the original point cloud on left side
    pl.subplot(0, 0)
    pl.add_mesh(
        pc_orig,
        scalars="z",                  # 按高度上色
        cmap="viridis",
        point_size=8,                 # 1-2 像素
        render_points_as_spheres=False, # 必须 False
        lighting=False,               # 关光照
        ambient=1.0                   # 环境光拉满，点云更亮
    )
    pl.add_text('original point cloud')
    pl.set_scale(xscale=10000.0, yscale=10000.0, zscale=1.0)
    pl.add_axes()
    pl.reset_camera()

    # ==================================================
    # plot the processed point cloud on right side
    pl.subplot(0, 1)
    pl.add_mesh(
        pc_processed,
        scalars="z",                  # 按高度上色
        cmap="viridis",
        point_size=8,                 # 1-2 像素
        render_points_as_spheres=False, # 必须 False
        lighting=False,               # 关光照
        ambient=1.0,                  # 环境光拉满，点云更亮
    )
    pl.add_text('processed point cloud')
    pl.set_scale(xscale=10000.0, yscale=10000.0, zscale=1.0)
    pl.add_axes()
    pl.reset_camera()

    # ==================================================

    pl.link_views()   # 所有子图相机联动
    pl.show()

