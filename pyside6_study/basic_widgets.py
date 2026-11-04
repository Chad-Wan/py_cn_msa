
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
import sys

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("try to push me!!", self)
        btn.setToolTip("why push me?")
        btn.setGeometry(100, 100, 200, 100)
        btn.setText('set text again')

        lb = QLabel('', self)
        lb.setText("this is a label")

        line = QLineEdit("")
        line.setPlaceholderText("this is a test.")




if __name__ == '__main__':
    my_app = QApplication(sys.argv)  ## inst a app class
    my_window = MyMainWindow()       ## inst a window
    my_window.show()
    my_app.exec()
