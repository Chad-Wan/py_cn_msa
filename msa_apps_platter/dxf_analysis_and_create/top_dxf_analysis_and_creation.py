import sys
import os
import pandas as pd
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox

from common_func.basic_func import browser_to_file
from common_func.basic_func import browser_to_folder
from .dxf_analysis_and_creation_ui import Ui_Form
import os
from ezdxf import recover
import ezdxf
from datetime import datetime

class SubWindowDxfRW(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.df_xtf_config_depth = pd.DataFrame({})
        self.df_xtf_config_svp = pd.DataFrame({})

        self.dxf_file_path_gp1 = ""
        self.output_path_gp1 = ""
        self.layer_processed_gp1 = ""
        self.comboBox_output_format_gp1.addItems([
            "各段折线简报",
            "cvs文件"
        ])

        self.cvs_file_path_gp2 = ""
        self.output_path_gp2 = ""
        self.layer_processed_gp2 = ""
        self.comboBox_remove_duplication_gp2.addItems([
            "是",
            "否"
        ])

        self.pushButton_browser_to_dxf_gp1.clicked.connect(self.browser_to_dxf_gp1)
        self.pushButton_browser_to_output_path_gp1.clicked.connect(self.browser_to_output_path_gp1)
        self.pushButton_start_output_pg1.clicked.connect(self.start_output_pg1)

        self.pushButton_browser_to_csv_gp2.clicked.connect(self.browser_to_csv_gp2)
        self.pushButton_browser_to_output_path_gp2.clicked.connect(self.browser_to_output_path_gp2)
        self.pushButton_start_output_gp2.clicked.connect(self.start_output_gp2)

    def browser_to_dxf_gp1(self):
        file_path = browser_to_file("dxf")
        if file_path is not None:
            self.dxf_file_path_gp1 = file_path
            self.lineEdit_dxf_path_gp1.setText(self.dxf_file_path_gp1)

    def browser_to_output_path_gp1(self):
        file_path = browser_to_folder()
        if file_path is not None:
            self.output_path_gp1 = file_path
            self.lineEdit_output_path_gp1.setText(self.output_path_gp1)

    def start_output_pg1(self):
        # file_path = self.lineEdit_dxf_path_gp1.text()
        # target_path = self.lineEdit_output_path_gp1.text()

        doc, auditor = recover.readfile(self.lineEdit_dxf_path_gp1.text())
        # if auditor.has_errors:
        #     auditor.print_error_report()

        msp = doc.modelspace()

        polyline_list = []

        # 遍历 LWPOLYLINE
        for pl in msp.query("LWPOLYLINE"):
            layer = pl.dxf.layer
            elev = pl.dxf.get("elevation", 0.0)
            pts_raw = pl.get_points()
            coords = []
            for p in pts_raw:
                x, y, _, _, _ = p
                coords.append((x, y, elev))
            polyline_list.append({
                "type": "LWPOLYLINE",
                "layer": layer,
                "points": coords
            })

        point_set = []

        gen_cvs_file = True
        lines = []

        output_format_1 = self.comboBox_output_format_gp1.currentText()
        if output_format_1 == "各段折线简报":
            gen_cvs_file = False

        line_nu = 1
        point_nu = 1
        if not gen_cvs_file:
            for idx, item in enumerate(polyline_list, start=1):
                if item["layer"] == self.lineEdit_target_layer_gp1.text():
                    lines.append(f"===== 第 {line_nu} 条折线 | 类型:{item['type']} | 图层:{item['layer']} =====\n")
                    pts = item["points"]
                    for i, (x, y, z) in enumerate(pts):
                        if i == 0:
                            tag = "[起点]"
                        elif i == len(pts) - 1:
                            tag = "[终点]"
                        else:
                            tag = "[折点]"
                        lines.append(f"{tag}  X:{x:.3f}, Y:{y:.3f}, Z:{z:.3f}\n")
                        point_nu += 1
                    lines.append("\n")
                    line_nu += 1
            f = open(self.lineEdit_output_path_gp1.text() + '/dxf_line_report.txt', "w")
            f.writelines(lines)
            f.close()
            QMessageBox.information(
                None,
                "提取完成",
                f"提取完成！\n一共提取到 {line_nu - 1} 条独立折线\n统计报告已经存储在" + self.output_path_gp1 + '/dxf_line_report.txt中.')
        else:
            for idx, item in enumerate(polyline_list, start=1):
                if item["layer"] == self.lineEdit_target_layer_gp1.text():
                    pts = item["points"]
                    for i, (x, y, z) in enumerate(pts):
                        point_set.append([line_nu, point_nu, x, y, z])
                        point_nu += 1
                    line_nu += 1
            df_points = pd.DataFrame(point_set, columns=["line_num", "point_num", "X", "Y", "Z"])
            # if self.comboBox_remove_duplication_gp2 == "是":
            #     df_points = df_points.drop_duplicates(subset=['X', 'Y'])
            print(df_points)

            df_points.to_csv(self.lineEdit_output_path_gp1.text() + "/dxf_points_report.csv", columns=["X", "Y"])

            QMessageBox.information(
                None,
                "提取完成",
                f"转换完成！\n一共提取到 {line_nu - 1} 条独立折线\n结果已经存储到" + self.output_path_gp1 + '/dxf_points_report.csv中')


    def browser_to_csv_gp2(self):
        file_path = browser_to_file("csv")
        if file_path is not None:
            self.cvs_file_path_gp2 = file_path
            self.lineEdit_csv_path_gp2.setText(self.cvs_file_path_gp2)

    def browser_to_output_path_gp2(self):
        file_path = browser_to_folder()
        if file_path is not None:
            self.output_path_gp2 = file_path
            self.lineEdit_output_path_gp2.setText(self.output_path_gp2)

    def start_output_gp2(self):
        input_path = self.lineEdit_csv_path_gp2.text()
        target_path = self.lineEdit_output_path_gp2.text() + '/output.dxf'

        df_points = pd.read_csv(input_path, header=None)
        df_points.columns = ['ind', 'X', 'Y']
        if self.comboBox_remove_duplication_gp2 == "是":
            df_points = df_points.drop_duplicates(subset=['X', 'Y'])
        point_list = df_points.values.tolist()
        # print(point_list)

        point_list = point_list[1:]

        doc = ezdxf.new("R2010")
        msp = doc.modelspace()

        target_layer = self.lineEdit_target_layer_gp2.text()
        doc.layers.add(target_layer, color=1)

        for idx, x, y in point_list:
            x_value = round(float(x),3)
            y_value = round(float(y),3)
            msp.add_point((x_value, y_value), dxfattribs={"layer": target_layer})
            msp.add_text(str(int(idx)), dxfattribs={"height": 2, "layer": target_layer}).set_placement((x_value + 1, y_value + 1))

        doc.saveas(target_path)
        QMessageBox.information(
            None,
            "操作成功",
            f"结果已经存储到" + target_path + '中')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SubWindowDxfRW()
    window.show()
    app.exec()