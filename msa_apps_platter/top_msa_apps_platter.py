import sys
from datetime import date

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from msa_apps_platter import Ui_MainWindow
from hvf_editor.top_hvf_editor import SubWindowHvfEditor
from field_collection_record_sheet.top_field_collection_recording_sheet_export import FC_RecordWindow
from caris_time_converter.top_caris_time_converter import SubWindowTimeConverter


class TopWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_hvf_editor.clicked.connect(self.show_hvf_editor)
        self.pushButton_xtf_to_recording.clicked.connect(self.show_xtf_to_recording)
        self.pushButton_caris_time_converter.clicked.connect(self.show_caris_time_converter)

        self.action_about_this_app.triggered.connect(self.show_about_this_app)


    def show_hvf_editor(self):
        self.sub_window_1 = SubWindowHvfEditor()
        self.sub_window_1.show()

    def show_xtf_to_recording(self):
        self.sub_window_2 = FC_RecordWindow()
        self.sub_window_2.show()

    def show_caris_time_converter(self):
        self.sub_window_3 = SubWindowTimeConverter()
        self.sub_window_3.show()

    def show_about_this_app(self):
        text = "Version 1.0\n\nHi,\n如果你知道我在哪，发现任何问题或者有什么疑问，可以直接来喊我。。\nEmail也行：wanchao9999@outlook.com\n工具只是辅助，人才是灵魂。\n祝好"
        QMessageBox.information(None, "关于这些脚本", text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TopWindow()
    window.show()
    sys.exit(app.exec())
