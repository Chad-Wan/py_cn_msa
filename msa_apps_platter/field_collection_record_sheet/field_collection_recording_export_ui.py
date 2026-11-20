# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'field_collection_recording_export_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(828, 264)
        self.pushButton_start_analysis = QPushButton(Form)
        self.pushButton_start_analysis.setObjectName(u"pushButton_start_analysis")
        self.pushButton_start_analysis.setGeometry(QRect(610, 180, 171, 41))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_start_analysis.setFont(font)
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
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 40, 741, 121))
        self.layoutWidget.setFont(font)
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_browser_to_xtf_folder = QPushButton(self.layoutWidget)
        self.pushButton_browser_to_xtf_folder.setObjectName(u"pushButton_browser_to_xtf_folder")
        self.pushButton_browser_to_xtf_folder.setFont(font)
        self.pushButton_browser_to_xtf_folder.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_browser_to_xtf_folder, 0, 2, 1, 1)

        self.lineEdit_xtf_location = QLineEdit(self.layoutWidget)
        self.lineEdit_xtf_location.setObjectName(u"lineEdit_xtf_location")
        self.lineEdit_xtf_location.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_xtf_location, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton_browser_to_excel_folder = QPushButton(self.layoutWidget)
        self.pushButton_browser_to_excel_folder.setObjectName(u"pushButton_browser_to_excel_folder")
        self.pushButton_browser_to_excel_folder.setFont(font)
        self.pushButton_browser_to_excel_folder.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_browser_to_excel_folder, 1, 2, 1, 1)

        self.lineEdit_excel_location = QLineEdit(self.layoutWidget)
        self.lineEdit_excel_location.setObjectName(u"lineEdit_excel_location")
        self.lineEdit_excel_location.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_excel_location, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5916\u4e1a\u91c7\u96c6\u8bb0\u5f55\u8868\u751f\u6210\u5668  -- by Mr. Wan", None))
        self.pushButton_start_analysis.setText(QCoreApplication.translate("Form", u"\u5206\u6790\u6570\u636e\u5e76\u6267\u884c", None))
        self.label.setText(QCoreApplication.translate("Form", u"XTF\u6587\u4ef6\u5939\u6240\u5728\u4f4d\u7f6e\uff1a", None))
        self.pushButton_browser_to_xtf_folder.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5c06excel\u8f93\u51fa\u81f3\u6587\u4ef6\u5939\uff1a", None))
        self.pushButton_browser_to_excel_folder.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
    # retranslateUi

