
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyMainWindow()
    my_window.show()
    app.exec()



