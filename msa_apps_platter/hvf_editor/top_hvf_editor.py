import sys
import os
import pandas as pd
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from .hvf_editor_ui import Ui_Form
from common_func.hvf import reorder_the_hvf_existing_settings_transducer
from common_func.hvf import generate_one_hvf_item_depth
from common_func.hvf import generate_one_hvf_item_svp
from common_func.hvf import read_hml, write_hml, str_datetime_to_str_doytime
from datetime import datetime

class SubWindowHvfEditor(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.df_xtf_config = pd.DataFrame({})

        self.pushButton_browser_to_hvf.clicked.connect(self.browser_to_file)
        self.pushButton_browser_to_xtf.clicked.connect(self.browser_to_xtf_folder)
        self.pushButton_start_analysis.clicked.connect(self.start_analysis)
        self.pushButton_start_read_hvf_file_according_to_xtf_file_list.clicked.connect(self.extract_xtf_file_info)
        self.pushButton_save_to_df.clicked.connect(self.save_to_df)
        self.pushButton_write_back_to_hvf.clicked.connect(self.save_to_hvf)
        self.pushButton_read_df_database.clicked.connect(self.read_df_database)


    def browser_to_file(self):
        file_path, filter_str = QFileDialog.getOpenFileName(
            None,
            "请选择数据文件",
            ".",
            "Config File(*.hvf);;All Files (*.*)"
        )
        if file_path and os.path.isfile(file_path):
            self.lineEdit_hvf_file_location.setText(file_path)

    def browser_to_xtf_folder(self):
        folder_path = QFileDialog.getExistingDirectory(
            None,
            "选择xtf所在文件夹（应包含所有需要的xtf文件)",
            "")
        if folder_path and os.path.isdir(folder_path):
            self.lineEdit_xtf_files_location_folder.setText(folder_path)

    def save_df_to_file(self, file_path: str):
        self.df_xtf_config.to_pickle(file_path)

    def generate_new_approximate_angle(self, old_angle: float):
        if old_angle < 22.5:
            new_angle = 0
        elif 22.5 <= old_angle < 67.5:
            new_angle = 45
        elif 67.5 <= old_angle < 112.5:
            new_angle = 90
        elif 112.5 <= old_angle < 157.5:
            new_angle = 135
        elif 157.5 <= old_angle < 202.5:
            new_angle = 180
        elif 202.5 <= old_angle < 247.5:
            new_angle = 225
        elif 247.5 <= old_angle < 292.5:
            new_angle = 270
        elif 292.5 <= old_angle < 337.5:
            new_angle = 315
        else:
            new_angle = 0
        return new_angle


    def angle_to_arrow(self, angle):
        """把角度归一化到 0~360 后映射到箭头。
        非 45° 倍数的角度会报错，方便发现脏数据。"""
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
        # 归一化：支持负数和超过 360 的值
        a = round(float(angle)) % 360
        if a not in ARROW_MAP:
            raise ValueError(f"角度 {angle}° 不是 45° 的倍数")
        return ARROW_MAP[a]



    def start_analysis(self):
        hvf_file_path = self.lineEdit_hvf_file_location.text()
        xtf_file_path = self.lineEdit_xtf_files_location_folder.text()
        self.pushButton_start_analysis.setEnabled(False)
        self.df_xtf_config = reorder_the_hvf_existing_settings_transducer(hvf_file_path, xtf_file_path)
        self.pushButton_start_analysis.setText("分析已经完成")
        self.generate_xtf_filelist()
        self.save_df_to_file(hvf_file_path + "_db")
        QMessageBox.information(
            None,
            "解析完成",
            "解析完成,数据库建立完成！")

    def generate_xtf_filelist(self):
        xtf_file_list = []
        for i in range(len(self.df_xtf_config)):
            xtf_file_list.append(self.df_xtf_config.loc[i, "file_name"])
        self.comboBox_available_xtf_file_names.addItems(xtf_file_list)

    def read_data_from_xtf_dataframe(self, file_name: str, output_text=True):
        # 这个函数用来读取xtf dataframe中的单条信息，以文件名为索引，提取xyz和pitch,roll,yaw并返回
        # 参数output_test可以控制返回的值是文本形式还是实际数据类型形式
        date_time_start = self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "start_time"].values[0]
        date_time_end = self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "end_time"].values[0]
        x = self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "X"].values[0]
        y = self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "Y"].values[0]
        z = self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "Z"].values[0]
        pitch = self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "pitch"].values[0]
        roll = self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "roll"].values[0]
        yaw = self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "yaw"].values[0]
        direction = self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "direction"].values[0]

        if output_text:
            date_time_start = str(date_time_start)
            date_time_end = str(date_time_end)
            x = str(x)
            y = str(y)
            z = str(z)
            pitch = str(pitch)
            roll = str(roll)
            yaw = str(yaw)
            return date_time_start, date_time_end, x, y, z, pitch, roll, yaw, direction
        else:
            return date_time_start, date_time_end, x, y, z, pitch, roll, yaw, direction

    def extract_xtf_file_info(self):
        # 将dataframe中的一条xtf相关配置读取出来，在lineEdit控件中显示出来
        file_name = self.comboBox_available_xtf_file_names.currentText()
        date_time_start, date_time_end, x, y, z, pitch, roll, yaw, direction = (
            self.read_data_from_xtf_dataframe(file_name, output_text=True))

        self.lineEdit_date.setText(date_time_start.split("T")[0])
        self.lineEdit_time.setText(date_time_start.split("T")[1].split('.')[0])
        self.lineEdit_x.setText(x)
        self.lineEdit_y.setText(y)
        self.lineEdit_z.setText(z)
        self.lineEdit_picth.setText(pitch)
        self.lineEdit_roll.setText(roll)
        self.lineEdit_yaw.setText(yaw)
        self.lineEdit_nav_direction.setText(str(int(direction)) + self.angle_to_arrow(self.generate_new_approximate_angle(direction)))

    def save_to_df(self):
        file_name = self.comboBox_available_xtf_file_names.currentText()
        [year, month, day] = self.lineEdit_date.text().split("-")
        [hour, minuit, second] = self.lineEdit_time.text().split(":")
        date_time = datetime(int(year), int(month), int(day), int(hour), int(minuit), int(second))
        x = float(self.lineEdit_x.text())
        y = float(self.lineEdit_y.text())
        z = float(self.lineEdit_z.text())
        pitch = float(self.lineEdit_picth.text())
        roll = float(self.lineEdit_roll.text())
        yaw = float(self.lineEdit_yaw.text())

        self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "X"] = x
        self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "Y"] = y
        self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "Z"] = z
        self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "pitch"] = pitch
        self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "roll"] = roll
        self.df_xtf_config.loc[self.df_xtf_config["file_name"] == file_name, "yaw"] = yaw



    def save_to_hvf(self):
        # 将所有xtf文件自己的配置写入一个列表，每个列表元素都是事先定义好的字典。后期直接写入hvf配置文件
        # 这个列表的名字叫做new_configs
        new_configs = []
        # print(self.df_xtf_config)
        self.save_df_to_file(self.lineEdit_hvf_file_location.text() + "_db")
        for xtf_file in self.df_xtf_config["file_name"]:
            file_name = xtf_file
            # print(file_name)
            date_time_start, date_time_end, x, y, z, pitch, roll, yaw, nothing = (
                self.read_data_from_xtf_dataframe(file_name,output_text=True))

            date_time_start = str_datetime_to_str_doytime(date_time_start)
            date_time_end = str_datetime_to_str_doytime(date_time_end)

            # print(date_time_start, date_time_end)
            new_configs.append(generate_one_hvf_item_depth(date_time_start, x, y, z, pitch, roll, yaw))
            new_configs.append(generate_one_hvf_item_depth(date_time_end, '0', '0', '0', '0', '0', '0'))

            # print(new_configs)

        # print(new_configs)

        # 解析全部hvf文件信息
        hvf_file_path = self.lineEdit_hvf_file_location.text()
        data = read_hml(hvf_file_path)
        # 将原来配置全部替换
        data['HIPSVesselConfig']['DepthSensor']['TimeStamp'] = new_configs
        # 将新生成的hvf文件写回原来位置
        # enableBackup用于设定是否将原来的hvf文件进行备份
        write_hml(hvf_file_path, data)

        QMessageBox.information(
            None,
            "写入完成",
            "写入完成！")

    def read_df_database(self):
        try:
            self.df_xtf_config = pd.read_pickle(self.lineEdit_hvf_file_location.text() + "_db")
            self.generate_xtf_filelist()
        except:
            QMessageBox.information(
                None,
                "读入失败",
                "读入失败，请查看hvf文件同级是否有hvf_db文件存在！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SubWindowHvfEditor()
    window.show()
    app.exec()
