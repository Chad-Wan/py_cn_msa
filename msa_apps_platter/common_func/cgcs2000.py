"""
CGCS2000 高斯-克吕格投影 正反算 & 换带工具
============================================
基准椭球 : CGCS2000 (a=6378137, f=1/298.257222101)
投影     : 高斯-克吕格 / 横墨卡托 (Transverse Mercator, 默认 k0=1)
y 约定   : 自然值(未加500km) <-> 通用值(500km加常数, 可选带号)

示例
----
from cgcs2000_gauss import CGCS2000Gauss

g = CGCS2000Gauss(L0=118.5)          # 自定义中央经线
x, y = g.bl2xy(38.299583, 118.113333)
B, L = g.xy2bl(x, y)                # 反算回经纬度

g39 = CGCS2000Gauss(zone=39, zone_width=3)   # 3度带39带
x2, y2 = g.transform_to(g39, x, y)           # 换带: 118.5E -> 39带
"""

import math
from typing import Tuple


class CGCS2000Gauss:
    """CGCS2000 椭球上的高斯投影正反算。"""

    # ---------- 椭球参数 ----------
    a = 6378137.0
    f = 1 / 298.257222101

    def __init__(self, L0: float = None, zone: int = None, zone_width: int = 3):
        """
        参数
        ----
        L0 : 中央经线(十进制度), 自定义投影直接给值, 如 118.5
        zone : 分带带号(与 L0 二选一). 3度带: 39带->117E; 6度带: 20带->117E
        zone_width : 3 或 6, 配合 zone 使用
        """
        if L0 is not None:
            self.L0 = float(L0)
        elif zone is not None:
            self.L0 = self.zone_to_L0(zone, zone_width)
        else:
            raise ValueError("必须提供 L0 或 (zone + zone_width)")

    # ---------- 分带工具 ----------
    @staticmethod
    def zone_to_L0(zone: int, zone_width: int = 3) -> float:
        """带号 -> 中央经线. 3度带: L0=3*zone; 6度带: L0=6*zone-3"""
        if zone_width == 3:
            return 3.0 * zone
        if zone_width == 6:
            return 6.0 * zone - 3.0
        raise ValueError("zone_width 只能是 3 或 6")

    @staticmethod
    def lon_to_zone(lon: float, zone_width: int = 3) -> int:
        """经度 -> 带号(向下取整). 实际选带需根据测区整体位置权衡."""
        if zone_width == 3:
            return int(math.floor(lon / 3.0)) + 1
        return int(math.floor(lon / 6.0)) + 1

    # ---------- 正算: BL -> xy ----------
    def bl2xy(self, B, L,
              with_500km: bool = False,
              with_zone: bool = False,
              zone: int = None) -> Tuple[float, float]:
        """
        经纬度(十进制度) -> 高斯平面坐标(m).

        参数
        ----
        with_500km : True 时 y 加 500000
        with_zone   : True 时 y 前加带号(需提供 zone, 自定义投影无意义)
        """
        e2 = self.f * (2 - self.f)
        B = math.radians(B)
        l = math.radians(L) - math.radians(self.L0)

        sinB, cosB = math.sin(B), math.cos(B)
        tanB = sinB / cosB
        N = self.a / math.sqrt(1 - e2 * sinB * sinB)
        t = tanB
        eta2 = e2 / (1 - e2) * cosB * cosB

        # 子午线弧长 X
        n = e2 / (2 - e2)
        a0 = 1 + n * n / 4 + n ** 4 / 64
        a2 = -3 / 2 * (n - n ** 3 / 8)
        a4 = 15 / 16 * (n * n - n ** 4 / 4)
        a6 = -35 / 48 * n ** 3
        X = self.a / (1 + n) * (
            a0 * B + a2 * math.sin(2 * B)
            + a4 * math.sin(4 * B) + a6 * math.sin(6 * B))

        l2, l4, l6 = l * l, l ** 4, l ** 6
        x = (X + N * t * cosB ** 2 / 2 * l2
             + N * t * (5 - t * t + 9 * eta2 + 4 * eta2 * eta2) / 24 * cosB ** 4 * l4
             + N * t * (61 - 58 * t * t + t ** 4) / 720 * cosB ** 6 * l6)

        y = (N * cosB * l
             + N * (1 - t * t + eta2) / 6 * cosB ** 3 * l2 * l
             + N * (5 - 18 * t * t + t ** 4 + 14 * eta2 - 58 * eta2 * t * t) / 120
             * cosB ** 5 * l4)

        if with_500km:
            y += 500000.0
        if with_zone:
            if zone is None:
                raise ValueError("带号投影需指定 zone")
            y += zone * 1_000_000.0
        return x, y

    # ---------- 反算: xy -> BL ----------
    def xy2bl(self, x: float, y: float,
              with_500km: bool = False,
              with_zone: bool = False) -> Tuple[float, float]:
        """
        高斯平面坐标(m) -> 经纬度(十进制度).

        参数
        ----
        with_500km : 输入 y 已加 500000, 先扣回
        with_zone   : 输入 y 带带号, 先去掉(要求 L0 为 None 或自定义)
        """
        if with_zone:
            y = y % 1_000_000.0
        if with_500km:
            y -= 500000.0

        e2 = self.f * (2 - self.f)
        ep2 = e2 / (1 - e2)

        # 底点纬度 Bf
        n = e2 / (2 - e2)
        a0 = 1 + n * n / 4 + n ** 4 / 64
        a2 = 3 / 2 * (n - n ** 3 / 8)
        a4 = 15 / 16 * (n * n - n ** 4 / 4)
        a6 = 35 / 48 * n ** 3
        Bf = (1 + n) * x / (self.a * a0)
        for _ in range(8):
            Bf = (1 + n) * x / (self.a * a0) - (a2 * math.sin(2 * Bf)
                                           + a4 * math.sin(4 * Bf)
                                           + a6 * math.sin(6 * Bf)) / a0

        sinBf, cosBf = math.sin(Bf), math.cos(Bf)
        tanBf = sinBf / cosBf
        Nf = self.a / math.sqrt(1 - e2 * sinBf * sinBf)
        t = tanBf
        t2, t4 = t * t, t ** 4
        eta2 = ep2 * cosBf * cosBf

        y_ = y / Nf
        y2, y3, y4, y5, y6 = y_ ** 2, y_ ** 3, y_ ** 4, y_ ** 5, y_ ** 6

        B = (Bf - t / (2 * Nf ** 2) * y2
             + t / (24 * Nf ** 4) * (5 + 3 * t2 + eta2 - 9 * eta2 * t2) * y4
             - t / (720 * Nf ** 6) * (61 + 90 * t2 + 45 * t4) * y6)

        l = (1 / (Nf * cosBf) * y
             - 1 / (6 * Nf ** 3 * cosBf) * (1 + 2 * t2 + eta2) * y3
             + 1 / (120 * Nf ** 5 * cosBf) * (5 + 28 * t2 + 24 * t4
                                               + 6 * eta2 + 8 * eta2 * t2) * y5)

        return math.degrees(B), math.degrees(l) + self.L0

    # ---------- 换带 ----------
    def transform_to(self, other, x: float, y: float,
                     with_500km: bool = False,
                     with_zone: bool = False) -> Tuple[float, float]:
        """先把 xy 反算成 BL, 再用 other 投影正算成新带 xy."""
        B, L = self.xy2bl(x, y, with_500km=with_500km, with_zone=with_zone)
        return other.bl2xy(B, L)

    def __repr__(self):
        return f"CGCS2000Gauss(L0={self.L0:.4f}°)"

def dms2deg(degrees: int, minutes: int, seconds: float) -> float:
    """度分秒 -> 十进制度: deg + min/60 + sec/3600"""
    return round(degrees + minutes / 60 + seconds / 3600, 8)

def deg2dms(deg:float):
    """十进制度 -> 度分秒: (degrees, minutes, seconds)"""
    sign = -1 if deg < 0 else 1
    d = int(deg)
    m = int((abs(deg) - abs(d)) * 60)
    s = round((abs(deg) - abs(d) - m / 60) * 3600, 4)
    return sign * d, m, s

# x = dms2deg(38,7,38.356)
# y = dms2deg(117,54,3.184)
# print(x, y)
# print(dms2deg(38,7,38.356))
# g = CGCS2000Gauss(L0=118.5)
# x,y = g.bl2xy(x, y, with_500km=True)
# print(x)
# print(y)