from datetime import date, timedelta
from PySide6.QtWidgets import QApplication, QWidget
from dateutil.utils import today
# from h5py.h5f import mount
from .caris_time_converter_ui import Ui_Form

class SubWindowTimeConverter(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.today = date.today()

        accepted_year = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
        accepted_month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        self.comboBox_year_to_conv_upper.addItems(accepted_year)
        self.comboBox_year_to_conv_upper.setCurrentIndex(self.today.year - 2024)

        self.comboBox_year_to_conv_lower.addItems(accepted_year)
        self.comboBox_year_to_conv_lower.setCurrentIndex(self.today.year - 2024)

        self.comboBox_mounth_to_conv_lower.addItems(accepted_month)
        self.comboBox_mounth_to_conv_lower.setCurrentIndex(self.today.month - 1)

        self.spinBox_day_to_conv_lower.setValue(self.today.day)
        self.spinBox_day_to_conv_upper.setValue(self.date_to_doy(self.today.year, self.today.month, self.today.day))

        self.pushButton_day_to_mmdd.clicked.connect(self.conv_doy_to_date)
        self.pushButton_mmdd_to_day.clicked.connect(self.conv_date_to_doy)


    def date_to_doy(self, year: int, month: int, day: int):
        dt = date(year, month, day)
        return dt.timetuple().tm_yday

    def doy_to_date(self, year: int, doy: int):
        dt = date(year, 1, 1)
        res = dt + timedelta(days=doy-1)
        return res

    def conv_doy_to_date(self):
        year = self.comboBox_year_to_conv_upper.currentText()
        doy = self.spinBox_day_to_conv_upper.value()
        res = self.doy_to_date(int(year), int(doy))

        self.label_conved_year_upper.setText(str(self.comboBox_year_to_conv_upper.currentText()))
        self.label_conved_month_upper.setText(str(res.month))
        self.label_conved_day_upper.setText(str(res.day))

    def conv_date_to_doy(self):
        year = self.comboBox_year_to_conv_lower.currentText()
        month = self.comboBox_mounth_to_conv_lower.currentText()
        day = self.spinBox_day_to_conv_lower.value()

        # print(year, month, day)

        doy = self.date_to_doy(int(year), int(month), int(day))
        self.label_conved_year_lower.setText(str(year))
        self.label_conved_day_lower.setText(str(doy))





