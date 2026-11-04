
# this is an algorithm set used to filter the noise/fake sonar points in multi-beam data.
# contact me please if there are any issues inside:
# email: wanchao9999@outlook.com




import numpy as np
from sklearn.neighbors import KDTree

# 趋势面约束 SOR
# 这是针对多波束复杂地形的改进版。
# 核心思想：先用二维网格拟合局部趋势面，计算残差，再对残差做 SOR。
# 这样陡坡上的真实点不会因为"距离邻居远"而被误删。
def shallow_water_sor_filter(
    points_ndarray,
    nb_neighbors=50,
    std_ratio=1.5,
    grid_res=6.0,
    max_grid_cells=500,
    max_depth_jump=5.0,
    min_depth=2.5,
    max_depth=30.0,
):
    """
    浅水多波束 SOR 滤波
    输入: (N, 3) ndarray, 列为 [经度, 纬度, 水深]
    返回: filtered_points (M, 3), stats (dict)
    """
    stats = {}
    N = len(points_ndarray)
    stats['original'] = N

    if N < nb_neighbors + 1:
        return np.empty((0, 3)), stats

    # ========== 1. 拆解列 ==========
    lon = points_ndarray[:, 0].astype(np.float64)
    lat = points_ndarray[:, 1].astype(np.float64)
    depth = points_ndarray[:, 2].astype(np.float64)

    # ========== 2. 经纬度 → 米 ==========
    lon0, lat0 = 117.81, 38.80
    meters_per_deg_lon = 86600.0
    meters_per_deg_lat = 111139.0

    easting  = (lon - lon0) * meters_per_deg_lon
    northing = (lat - lat0) * meters_per_deg_lat

    # ========== 3. 深度有效性预筛 ==========
    valid = (depth >= min_depth) & (depth <= max_depth) & np.isfinite(depth)
    stats['after_depth_check'] = valid.sum()

    if valid.sum() < nb_neighbors + 1:
        return np.empty((0, 3)), stats

    e = easting[valid]
    n = northing[valid]
    d = depth[valid]

    # ========== 4. 趋势面拟合 ==========
    e_min, e_max = e.min(), e.max()
    n_min, n_max = n.min(), n.max()

    e_range = e_max - e_min
    n_range = n_max - n_min

    nx = min(int(np.ceil(e_range / grid_res)), max_grid_cells)
    ny = min(int(np.ceil(n_range / grid_res)), max_grid_cells)
    nx = max(nx, 2)
    ny = max(ny, 2)

    H, xe, ye = np.histogram2d(e, n, bins=[nx, ny], weights=d)
    counts, _, _ = np.histogram2d(e, n, bins=[nx, ny])
    trend_grid = H / np.maximum(counts, 1)

    x_centers = (xe[:-1] + xe[1:]) / 2
    y_centers = (ye[:-1] + ye[1:]) / 2
    Xc, Yc = np.meshgrid(x_centers, y_centers)

    # 硬裁剪，防止插值越界
    e = np.clip(e, x_centers[0], x_centers[-1])
    n = np.clip(n, y_centers[0], y_centers[-1])

    # ========== 5. 双线性插值 + 残差 ==========
    d_trend = _bilinear_interp(Xc, Yc, trend_grid, e, n)
    residual = d - d_trend

    # ========== 6. 残差 SOR ==========
    res_mean = np.nanmean(residual)
    res_std = np.nanstd(residual)
    threshold = res_std * std_ratio

    sor_mask = np.abs(residual - res_mean) <= threshold
    stats['after_sor'] = sor_mask.sum()

    # ========== 7. 深度跳变检查（内存安全版）==========
    e_clean = e[sor_mask]
    n_clean = n[sor_mask]
    d_clean = d[sor_mask]
    M = len(d_clean)

    if M > nb_neighbors:
        # 构建 KDTree（只用 2D 坐标）
        tree = KDTree(np.column_stack([e_clean, n_clean]))
        k = min(nb_neighbors + 1, M)

        # ★ 分批查询，避免一次性分配大数组
        batch_size = 50000  # 每批 5 万点
        depth_diff = np.empty(M, dtype=np.float32)

        for start in range(0, M, batch_size):
            end = min(start + batch_size, M)
            batch = np.column_stack([e_clean[start:end], n_clean[start:end]])

            # ★ 正确写法：idx shape = (batch, k)，取邻居的深度值
            dist, idx = tree.query(batch, k=k)

            # 排除自身（第 0 列是自身），计算与邻居的深度差
            neighbor_depths = d_clean[idx[:, 1:]]   # shape (batch, k-1)
            batch_diff = np.abs(
                d_clean[start:end, None] - neighbor_depths
            ).mean(axis=1)  # shape (batch,)

            depth_diff[start:end] = batch_diff.astype(np.float32)

        jump_mask = depth_diff <= max_depth_jump
    else:
        jump_mask = np.ones(M, dtype=bool)

    stats['after_jump_check'] = jump_mask.sum()

    # ========== 8. 合并结果 ==========
    final_valid = np.zeros(valid.sum(), dtype=bool)
    final_valid[sor_mask] = jump_mask

    keep_idx = np.where(valid)[0][final_valid]
    filtered_points = points_ndarray[keep_idx].copy()

    stats['final'] = len(filtered_points)
    stats['removed'] = N - len(filtered_points)

    return filtered_points, stats


def _bilinear_interp(Xc, Yc, grid, x, y):
    """
    双线性插值（安全版，绝不越界）
    Xc, Yc: meshgrid 后的网格中心坐标, shape (ny, nx)
    grid:    网格值, shape (ny, nx)
    x, y:    待插值点坐标, 1D array
    """
    ny, nx = grid.shape

    xi = np.searchsorted(Xc[0, :], x) - 1
    yi = np.searchsorted(Yc[:, 0], y) - 1

    xi = np.clip(xi, 0, nx - 2)
    yi = np.clip(yi, 0, ny - 2)

    x0 = Xc[0, xi]
    x1 = Xc[0, xi + 1]
    dx = (x - x0) / np.maximum(x1 - x0, 1e-12)
    dx = np.clip(dx, 0.0, 1.0)

    y0 = Yc[yi, 0]
    y1 = Yc[yi + 1, 0]
    dy = (y - y0) / np.maximum(y1 - y0, 1e-12)
    dy = np.clip(dy, 0.0, 1.0)

    val = (
        grid[yi, xi] * (1 - dx) * (1 - dy)
        + grid[yi, xi + 1] * dx * (1 - dy)
        + grid[yi + 1, xi] * (1 - dx) * dy
        + grid[yi + 1, xi + 1] * dx * dy
    )
    return val






def traditional_sor_filter(
    points_ndarray,
    nb_neighbors=30,
    std_ratio=2.0,
    batch_size=50000,
):
    """
    传统统计离群点移除 (Statistical Outlier Removal)

    对每个点找 K 个最近邻 → 计算到邻居的平均距离 → 剔除平均距离 > μ + α·σ 的点

    参数:
        points_ndarray: (N, 3) ndarray, 列为 [经度, 纬度, 水深]
        nb_neighbors:   K 近邻数量（不含自身，实际查 K+1）
        std_ratio:      α，阈值系数，通常 1.0~3.0
        batch_size:     分批查询大小，控制内存

    返回:
        filtered_points: (M, 3) ndarray，滤波后的点
        stats:           dict，各阶段统计
    """
    stats = {}
    N = len(points_ndarray)
    stats['original'] = N

    if N < nb_neighbors + 2:
        return np.empty((0, 3)), stats

    # ========== 1. 拆解 + 转近似米坐标 ==========
    lon  = points_ndarray[:, 0].astype(np.float64)
    lat  = points_ndarray[:, 1].astype(np.float64)
    depth = points_ndarray[:, 2].astype(np.float64)

    # 有效性检查
    valid = np.isfinite(lon) & np.isfinite(lat) & np.isfinite(depth)
    valid &= (depth > 0) & (depth < 100)  # 浅水合理范围
    stats['after_validity'] = valid.sum()

    if valid.sum() < nb_neighbors + 2:
        return np.empty((0, 3)), stats

    lon_v  = lon[valid]
    lat_v  = lat[valid]
    depth_v = depth[valid]

    # 天津附近近似转米
    lon0, lat0 = 117.81, 38.80
    x = (lon_v - lon0) * 86600.0
    y = (lat_v - lat0) * 111139.0
    z = depth_v  # 水深作为 z（单位已经是米，和 xy 一致）

    xyz = np.column_stack([x, y, z]).astype(np.float32)

    # ========== 2. 构建 KDTree ==========
    tree = KDTree(xyz)

    # ========== 3. 分批查询 K 近邻的平均距离 ==========
    M = len(xyz)
    k = nb_neighbors + 1  # +1 包含自身

    mean_dist = np.empty(M, dtype=np.float32)

    for start in range(0, M, batch_size):
        end = min(start + batch_size, M)
        batch = xyz[start:end]

        dist, idx = tree.query(batch, k=k)  # dist shape: (batch, k)

        # 排除自身（第 0 列），计算平均距离
        mean_dist[start:end] = dist[:, 1:].mean(axis=1)

    # ========== 4. 统计阈值 ==========
    mu = mean_dist.mean()
    sigma = mean_dist.std()
    threshold = mu + std_ratio * sigma

    stats['mean_distance_mu'] = float(mu)
    stats['std_distance'] = float(sigma)
    stats['threshold'] = float(threshold)

    # ========== 5. 剔除离群点 ==========
    keep_mask = mean_dist <= threshold
    stats['after_sor'] = keep_mask.sum()
    stats['removed'] = M - keep_mask.sum()

    # ========== 6. 映射回原始索引 ==========
    valid_idx = np.where(valid)[0]
    keep_idx = valid_idx[keep_mask]
    filtered_points = points_ndarray[keep_idx].copy()

    stats['final'] = len(filtered_points)

    return filtered_points, stats


# 连通量分析算法
# 对每个点找半径 r 内的邻居
# 如果两个点互为邻居 → 连一条边 → 构成图
# 用 BFS/DFS 找连通分量（每个连通分量 = 一个簇）
# 点数少于阈值的簇 → 判定为孤岛噪声，删除
def remove_islands_connected_components(
    points_ndarray,
    radius=3.0,
    min_cluster_size=30,
    batch_size=100000,
):
    """
    基于连通分量分析的孤岛噪声滤除（适合千万级点云）

    参数:
        points_ndarray:   (N, 3) ndarray
        radius:           连通半径（米）
        min_cluster_size: 少于这个点数 → 判定为孤岛，删除
        batch_size:       分批处理大小
    """
    N = len(points_ndarray)

    # 1. 转米坐标
    lon0, lat0 = 117.81, 38.80
    x = (points_ndarray[:, 0] - lon0) * 86600.0
    y = (points_ndarray[:, 1] - lat0) * 111139.0
    z = points_ndarray[:, 2]
    xyz = np.column_stack([x, y, z]).astype(np.float32)

    # 2. 构建 KDTree
    tree = KDTree(xyz)

    # 3. BFS 找连通分量（分批避免递归深度问题）
    visited = np.zeros(N, dtype=bool)
    labels = np.full(N, -1, dtype=np.int32)
    current_label = 0

    for i in range(N):
        if visited[i]:
            continue

        # BFS 从这个点开始
        cluster_indices = []
        queue = [i]
        visited[i] = True

        head = 0
        while head < len(queue):
            idx = queue[head]
            head += 1
            cluster_indices.append(idx)

            # 找邻居（分批 query 避免大数组）
            neighbors = tree.query_radius(xyz[idx:idx+1], r=radius)[0]
            for nbr in neighbors:
                if not visited[nbr]:
                    visited[nbr] = True
                    queue.append(nbr)

        # 标记这个簇
        if len(cluster_indices) >= min_cluster_size:
            labels[cluster_indices] = current_label
            current_label += 1

    # 4. 过滤
    keep_mask = labels >= 0
    filtered_points = points_ndarray[keep_mask]

    n_clusters = current_label
    noise_points = (~keep_mask).sum()

    stats = {
        'total_points': N,
        'kept_points': keep_mask.sum(),
        'noise_points': noise_points,
        'n_clusters': n_clusters,
        'noise_clusters': N - keep_mask.sum() > 0,
    }

    return filtered_points, stats, labels

