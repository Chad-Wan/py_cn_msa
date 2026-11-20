from datetime import date, timedelta
from PySide6.QtWidgets import QApplication, QWidget
from common_func.basic_func import browser_to_file
from common_func.basic_func import browser_to_folder
from common_func.basic_func import message_box
from dateutil.utils import today
# from h5py.h5f import mount
from .add_to_svp_ui import Ui_Form

class SVPAdder(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # button connections

