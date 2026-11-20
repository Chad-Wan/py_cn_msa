from datetime import date, timedelta
from PySide6.QtWidgets import QApplication, QWidget
from dateutil.utils import today
from common_func.basic_func import browser_to_file, browser_to_folder, message_box
from common_func.basic_func import str2float, float2str
from common_func.basic_func import read_file
# from h5py.h5f import mount
import re
from .add_to_tid_ui import Ui_Form

class TidAdder(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_browser_to_new_tid.clicked.connect(self.browser_to_new_tid)
        self.pushButton_browser_to_old_tid.clicked.connect(self.browser_to_old_tid)
        self.pushButton_start_add.clicked.connect(self.start_add)

        self.lineEdit_new_tid_file_path.setText("/home/wan/temp/demo潮位/潮位原始数据.txt")
        self.lineEdit_local_tid_file_path.setText("/home/wan/temp/demo潮位/test.txt")

    def browser_to_new_tid(self):
        file_path, file_str = browser_to_file()
        self.lineEdit_new_tid_file_path.setText(file_path)

    def browser_to_old_tid(self):
        file_path, file_str = browser_to_file()
        self.lineEdit_local_tid_file_path.setText(file_path)

    def start_add(self):
        k_value = str2float(self.lineEdit_k_value.text())
        c_value = str2float(self.lineEdit_C_value.text())

        old_lines = read_file(self.lineEdit_local_tid_file_path.text())
        print(self.lineEdit_local_tid_file_path.text())
        new_lines = read_file(self.lineEdit_new_tid_file_path.text())

        # for old_line in old_lines:
        #     try:
        #         t_date, t_time, t_tid = old_line.replace('\t', ' ').split(' ')
        #         print(t_date, t_time, t_tid)
        #     except:
        #         print("error:", old_line)
        #         continue

        for new_line in new_lines:
            try:
                new_line = re.sub(r'\t+', ' ', new_line)
                [t_date, t_time, t_tid] = new_line.split(' ')
                print(t_date, t_time, t_tid)
            except:
                print(new_line.replace('\t', ' ').split(' '))
                print("error:", new_line)
                continue


