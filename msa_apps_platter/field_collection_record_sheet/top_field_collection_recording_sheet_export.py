from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QMessageBox
from .field_collection_recording_export_ui import Ui_Form
import os
import pandas as pd
import openpyxl
from openpyxl.styles import Alignment, Font
from common_func.basic_func import find_all_subfiles_with_certain_patterns
from common_func.pyxtf_multibeam import get_single_multibeam_scan_recording


def angle_to_arrow(angle):
    """把角度归一化到 0~360 后映射到箭头。
    非 45° 倍数的角度会报错，方便你发现脏数据。"""
    # 归一化：支持负数和超过 360 的值
    ARROW_MAP = {
        90: "→",
        45: "↗",
        0: "↑",
        315: "↖",
        270: "←",
        225: "↙",
        180: "↓",
        135: "↘",
    }
    a = round(float(angle)) % 360
    if a not in ARROW_MAP:
        raise ValueError(f"角度 {angle}° 不是 45° 的倍数")
    return ARROW_MAP[a]


class FC_RecordWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.xtf_folder_path = ""
        self.excel_folder_path = ""

        self.pushButton_browser_to_xtf_folder.clicked.connect(self.browser_to_xtf_folder)
        self.pushButton_browser_to_excel_folder.clicked.connect(self.browser_to_excel_folder)
        self.lineEdit_xtf_location.textEdited.connect(self.lineEdit_xtf_location_changed)
        self.lineEdit_excel_location.textEdited.connect(self.lineEdit_excel_location_changed)
        self.pushButton_start_analysis.clicked.connect(self.start_analysis)

    def browser_to_xtf_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None,"选择xtf所在文件夹（应包含所有需要的xtf文件","")
        if folder_path and os.path.isdir(folder_path):
            self.lineEdit_xtf_location.setText(folder_path)
            self.xtf_folder_path = folder_path

    def browser_to_excel_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "选择excel将要输出的文件夹", "")
        if folder_path and os.path.isdir(folder_path):
            self.lineEdit_excel_location.setText(folder_path)
            self.excel_folder_path = folder_path

    def lineEdit_xtf_location_changed(self):
        self.xtf_folder_path = self.lineEdit_xtf_location.text()

    def lineEdit_excel_location_changed(self):
        self.excel_folder_path = self.lineEdit_excel_location.text()


    def start_analysis(self):
        # 找到lineedit里面标定文件夹以下，所有的xtf文件
        xtf_file_paths = find_all_subfiles_with_certain_patterns(self.xtf_folder_path, ".xtf")
        xtf_file_paths.sort()
        scan_record = []
        print(xtf_file_paths)

        for file in xtf_file_paths:
            scan_record.append(get_single_multibeam_scan_recording(file))
            print(file, " is done")

        df = pd.DataFrame(scan_record, columns=["文件名", "上线时间", "下线时间", "椭球面距离", "航向", "近似航向"])
        df.to_excel(self.excel_folder_path + "/测绘记录表.xlsx")

        # ========== 添加箭头 ==========
        # ========== 配置 ==========
        INPUT_FILE = self.excel_folder_path + "/测绘记录表.xlsx"  # 输入文件
        OUTPUT_FILE = self.excel_folder_path + "/测绘记录表_加箭头.xlsx"
        SHEET = "Sheet1"  # 工作表名
        ANGLE_COL = "G"  # 角度所在列
        ARROW_COL = "H"  # 箭头输出列

        # 8 方向箭头映射（角度：0°=东，逆时针为正）
        ARROW_MAP = {
            90: "→",
            45: "↗",
            0: "↑",
            315: "↖",
            270: "←",
            225: "↙",
            180: "↓",
            135: "↘",
        }
        # ==========================

        wb = openpyxl.load_workbook(INPUT_FILE)
        ws = wb[SHEET]

        # 找角度列的列号，方便定位箭头列
        angle_col_idx = openpyxl.utils.column_index_from_string(ANGLE_COL)
        arrow_col_idx = openpyxl.utils.column_index_from_string(ARROW_COL)

        # 跳过表头，从第 2 行开始
        for row in range(2, ws.max_row + 1):
            cell = ws.cell(row=row, column=angle_col_idx)
            if cell.value is None:
                continue
            try:
                arrow = angle_to_arrow(cell.value)
            except ValueError as e:
                arrow = "?"  # 非 45° 倍数，标记出来
                print(f"第 {row} 行: {e}")

            out = ws.cell(row=row, column=arrow_col_idx, value=arrow)
            out.alignment = Alignment(horizontal="center", vertical="center")
            out.font = Font(size=14)

        wb.save(OUTPUT_FILE)
        print(f"完成，已保存到 {OUTPUT_FILE}")
        QMessageBox.information(None, "导出完成", "文件已成功导出！")



