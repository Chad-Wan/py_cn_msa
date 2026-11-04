# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hvf_editor_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1014, 547)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 971, 501))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"Adwaita Sans"])
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, 9, -1)
        self.pushButton_browser_to_xtf = QPushButton(self.groupBox)
        self.pushButton_browser_to_xtf.setObjectName(u"pushButton_browser_to_xtf")
        self.pushButton_browser_to_xtf.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    color: #222222;\n"
"    border: 1px solid rgb(140,140,140);\n"
"    padding: 4px;\n"
"    border-radius: 4px;  /* \u5706\u89d2\uff0c0=\u76f4\u89d2 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,230,230);\n"
"    border:1px solid rgb(100,100,100); /* hover\u65f6\u8fb9\u6846\u53d8\u6df1 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,200,200);\n"
"    border:1px solid rgb(70,70,70);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_browser_to_xtf, 1, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.lineEdit_hvf_file_location = QLineEdit(self.groupBox)
        self.lineEdit_hvf_file_location.setObjectName(u"lineEdit_hvf_file_location")

        self.gridLayout.addWidget(self.lineEdit_hvf_file_location, 0, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        font1 = QFont()
        font1.setFamilies([u"Adwaita Sans"])
        font1.setPointSize(13)
        self.label_13.setFont(font1)

        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 3)

        self.lineEdit_xtf_files_location_folder = QLineEdit(self.groupBox)
        self.lineEdit_xtf_files_location_folder.setObjectName(u"lineEdit_xtf_files_location_folder")

        self.gridLayout.addWidget(self.lineEdit_xtf_files_location_folder, 1, 1, 1, 1)

        self.pushButton_browser_to_hvf = QPushButton(self.groupBox)
        self.pushButton_browser_to_hvf.setObjectName(u"pushButton_browser_to_hvf")
        self.pushButton_browser_to_hvf.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    color: #222222;\n"
"    border: 1px solid rgb(140,140,140);\n"
"    padding: 4px;\n"
"    border-radius: 4px;  /* \u5706\u89d2\uff0c0=\u76f4\u89d2 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,230,230);\n"
"    border:1px solid rgb(100,100,100); /* hover\u65f6\u8fb9\u6846\u53d8\u6df1 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,200,200);\n"
"    border:1px solid rgb(70,70,70);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_browser_to_hvf, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.pushButton_read_df_database = QPushButton(self.groupBox)
        self.pushButton_read_df_database.setObjectName(u"pushButton_read_df_database")
        self.pushButton_read_df_database.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    color: #222222;\n"
"    border: 1px solid rgb(140,140,140);\n"
"    padding: 4px;\n"
"    border-radius: 4px;  /* \u5706\u89d2\uff0c0=\u76f4\u89d2 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,230,230);\n"
"    border:1px solid rgb(100,100,100); /* hover\u65f6\u8fb9\u6846\u53d8\u6df1 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,200,200);\n"
"    border:1px solid rgb(70,70,70);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_read_df_database, 5, 2, 1, 1)

        self.pushButton_start_analysis = QPushButton(self.groupBox)
        self.pushButton_start_analysis.setObjectName(u"pushButton_start_analysis")
        self.pushButton_start_analysis.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    color: #222222;\n"
"    border: 1px solid rgb(140,140,140);\n"
"    padding: 4px;\n"
"    border-radius: 4px;  /* \u5706\u89d2\uff0c0=\u76f4\u89d2 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,230,230);\n"
"    border:1px solid rgb(100,100,100); /* hover\u65f6\u8fb9\u6846\u53d8\u6df1 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,200,200);\n"
"    border:1px solid rgb(70,70,70);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_start_analysis, 5, 0, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 7)
        self.gridLayout.setColumnStretch(2, 1)

        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, -1, 9, -1)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_available_xtf_file_names = QComboBox(self.groupBox_2)
        self.comboBox_available_xtf_file_names.setObjectName(u"comboBox_available_xtf_file_names")

        self.gridLayout_2.addWidget(self.comboBox_available_xtf_file_names, 0, 1, 1, 1)

        self.pushButton_start_read_hvf_file_according_to_xtf_file_list = QPushButton(self.groupBox_2)
        self.pushButton_start_read_hvf_file_according_to_xtf_file_list.setObjectName(u"pushButton_start_read_hvf_file_according_to_xtf_file_list")
        self.pushButton_start_read_hvf_file_according_to_xtf_file_list.setFont(font)
        self.pushButton_start_read_hvf_file_according_to_xtf_file_list.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    color: #222222;\n"
"    border: 1px solid rgb(140,140,140);\n"
"    padding: 4px;\n"
"    border-radius: 4px;  /* \u5706\u89d2\uff0c0=\u76f4\u89d2 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,230,230);\n"
"    border:1px solid rgb(100,100,100); /* hover\u65f6\u8fb9\u6846\u53d8\u6df1 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,200,200);\n"
"    border:1px solid rgb(70,70,70);\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_start_read_hvf_file_according_to_xtf_file_list, 0, 2, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 8)
        self.gridLayout_2.setColumnStretch(2, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_y = QLineEdit(self.groupBox_2)
        self.lineEdit_y.setObjectName(u"lineEdit_y")

        self.gridLayout_3.addWidget(self.lineEdit_y, 1, 3, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_nav_direction = QLineEdit(self.groupBox_2)
        self.lineEdit_nav_direction.setObjectName(u"lineEdit_nav_direction")
        self.lineEdit_nav_direction.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_nav_direction, 0, 5, 1, 1)

        self.lineEdit_date = QLineEdit(self.groupBox_2)
        self.lineEdit_date.setObjectName(u"lineEdit_date")
        self.lineEdit_date.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_date, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_6, 1, 2, 1, 1)

        self.lineEdit_x = QLineEdit(self.groupBox_2)
        self.lineEdit_x.setObjectName(u"lineEdit_x")

        self.gridLayout_3.addWidget(self.lineEdit_x, 1, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 4, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 1, 4, 1, 1)

        self.lineEdit_time = QLineEdit(self.groupBox_2)
        self.lineEdit_time.setObjectName(u"lineEdit_time")
        self.lineEdit_time.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEdit_time, 0, 3, 1, 1)

        self.lineEdit_z = QLineEdit(self.groupBox_2)
        self.lineEdit_z.setObjectName(u"lineEdit_z")

        self.gridLayout_3.addWidget(self.lineEdit_z, 1, 5, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 2, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_11, 2, 4, 1, 1)

        self.lineEdit_picth = QLineEdit(self.groupBox_2)
        self.lineEdit_picth.setObjectName(u"lineEdit_picth")

        self.gridLayout_3.addWidget(self.lineEdit_picth, 2, 1, 1, 1)

        self.lineEdit_roll = QLineEdit(self.groupBox_2)
        self.lineEdit_roll.setObjectName(u"lineEdit_roll")

        self.gridLayout_3.addWidget(self.lineEdit_roll, 2, 3, 1, 1)

        self.lineEdit_yaw = QLineEdit(self.groupBox_2)
        self.lineEdit_yaw.setObjectName(u"lineEdit_yaw")

        self.gridLayout_3.addWidget(self.lineEdit_yaw, 2, 5, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 3)
        self.gridLayout_3.setColumnStretch(2, 3)
        self.gridLayout_3.setColumnStretch(3, 3)
        self.gridLayout_3.setColumnStretch(4, 3)
        self.gridLayout_3.setColumnStretch(5, 3)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_save_to_df = QPushButton(self.groupBox_2)
        self.pushButton_save_to_df.setObjectName(u"pushButton_save_to_df")
        self.pushButton_save_to_df.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    color: #222222;\n"
"    border: 1px solid rgb(140,140,140);\n"
"    padding: 4px;\n"
"    border-radius: 4px;  /* \u5706\u89d2\uff0c0=\u76f4\u89d2 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,230,230);\n"
"    border:1px solid rgb(100,100,100); /* hover\u65f6\u8fb9\u6846\u53d8\u6df1 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,200,200);\n"
"    border:1px solid rgb(70,70,70);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_save_to_df)

        self.pushButton_write_back_to_hvf = QPushButton(self.groupBox_2)
        self.pushButton_write_back_to_hvf.setObjectName(u"pushButton_write_back_to_hvf")
        self.pushButton_write_back_to_hvf.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    color: #222222;\n"
"    border: 1px solid rgb(140,140,140);\n"
"    padding: 4px;\n"
"    border-radius: 4px;  /* \u5706\u89d2\uff0c0=\u76f4\u89d2 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(230,230,230);\n"
"    border:1px solid rgb(100,100,100); /* hover\u65f6\u8fb9\u6846\u53d8\u6df1 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(200,200,200);\n"
"    border:1px solid rgb(70,70,70);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_write_back_to_hvf)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 6)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"hvf\u7f16\u8f91\u5668 by Mr. Wan", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Step 1. \u914d\u7f6e", None))
        self.pushButton_browser_to_xtf.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"xtf\u6587\u4ef6\u5730\u5740:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"NOTE\uff1a\u8bf7\u786e\u4fdd\u6240\u6709\u7684xtf\u6587\u4ef6\u90fd\u5728\u4ee5\u4e0a\u7684\u8def\u5f84\u4e2d\uff08\u5728\u4ee5\u4e0a\u8def\u5f84\u7684\u5b50\u6587\u4ef6\u5939\u4e2d\u4e5f\u53ef\u4ee5\u3002\u3002\u3002\uff09", None))
        self.pushButton_browser_to_hvf.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"hvf\u6587\u4ef6\u4f4d\u7f6e\uff1a", None))
        self.pushButton_read_df_database.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6\u6570\u636e\u5e93", None))
        self.pushButton_start_analysis.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u89e3\u6790\u5e76\u5efa\u7acbxtf\u6570\u636e\u5e93(\u4ec5\u7b2c\u4e00\u6b21\u4f7f\u7528\u65f6\u9700\u8981\u4f7f\u7528)", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Step 2. \u8bfb/\u5199hvf\u6570\u636e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u76ee\u6807xtf\u6587\u4ef6\uff1a", None))
        self.pushButton_start_read_hvf_file_according_to_xtf_file_list.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8bfb\u5165", None))
        self.label.setText(QCoreApplication.translate("Form", u"date", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"X(m)", None))
        self.lineEdit_nav_direction.setText(QCoreApplication.translate("Form", u"NA", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"time", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Y(m)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u822a\u5411\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Z(m)", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Pitch", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Roll", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Yaw", None))
        self.pushButton_save_to_df.setText(QCoreApplication.translate("Form", u"\u5b58\u5165\u6570\u636e\u5e93", None))
        self.pushButton_write_back_to_hvf.setText(QCoreApplication.translate("Form", u"\u5df2\u7ecf\u6539\u597d\uff0c\u6570\u636e\u5e93\u540c\u6b65\u5230hvf\u6587\u4ef6\u4e2d", None))
    # retranslateUi

