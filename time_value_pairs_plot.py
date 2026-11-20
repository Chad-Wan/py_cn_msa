import numpy as np
import matplotlib.pyplot as plt


def beam_depth_tilted(theta_deg, z0, tilt_deg=15, roll_offset_deg=0):
    """
    theta_deg : 波束相对换能器阵面的跨航迹角 (°)
    tilt_deg  : 换能器固定斜发射倾角 15°
    roll_offset_deg : roll安装偏差
    return: 观测水深
    """
    theta = np.radians(theta_deg)
    tilt  = np.radians(tilt_deg)
    dr    = np.radians(roll_offset_deg)

    # 波束在空间的总俯仰角（阵面倾角+波束角），roll引入横向倾斜投影
    # roll偏差带来横向高程畸变，斜头下放大效应
    R = z0 / np.cos(tilt + theta)
    # roll引起垂直高度变化
    z_obs = R * np.cos(theta + dr)
    return z_obs

def svp_smile_tilted(theta_deg, z0, tilt_deg=15, svp_err_scale=0.12):
    """斜发射下SVP误差对称笑脸，斜头入射角更大，误差比正下视更明显"""
    theta = np.radians(theta_deg)
    tilt  = np.radians(tilt_deg)
    inc_angle = tilt + theta
    err = svp_err_scale * z0 * (np.abs(np.sin(inc_angle))**2.2)
    return z0 - err

# -------- 参数设置 --------
theta_arr = np.linspace(-55, 55, 300)  # 波束相对阵面跨航迹角
z0 = 5.0
tilt = 15

z_none    = beam_depth_tilted(theta_arr, z0, tilt, roll_offset_deg=0.0)
z_roll1p5 = beam_depth_tilted(theta_arr, z0, tilt, roll_offset_deg=1.5)
z_rolln1p5= beam_depth_tilted(theta_arr, z0, tilt, roll_offset_deg=-1.5)
z_smile   = svp_smile_tilted(theta_arr, z0, tilt, svp_err_scale=0.12)

# -------- 绘图 --------
fig, ax = plt.subplots(figsize=(11,6))
ax.plot(theta_arr, z_none,    'k-', lw=2.2, label='无 Roll Offset｜15°斜发射')
ax.plot(theta_arr, z_roll1p5, 'r-', lw=2.2, label='Roll Offset +1.5°｜15°斜发射')
ax.plot(theta_arr, z_rolln1p5,'g--',lw=2.2, label='Roll Offset -1.5°｜反向测线等效')
ax.plot(theta_arr, z_smile,   'b-.',lw=2.2, label='SVP误差笑脸｜15°斜发射')

ax.set_xlabel('波束相对阵面跨航迹角 θ (°)  Port ← 0 → Stbd')
ax.set_ylabel('观测水深 (m)')
ax.set_title('15°斜发射换能器：Roll Offset 偏差剖面对比（平底）')
ax.invert_yaxis()
ax.grid(True, alpha=0.3)
ax.legend()
plt.tight_layout()
plt.show()
