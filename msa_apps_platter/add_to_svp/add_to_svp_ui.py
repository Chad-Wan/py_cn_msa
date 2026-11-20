# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_to_svp_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(674, 315)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_5.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5c06\u65b0\u6f6e\u4f4d\u6587\u4ef6", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8ffd\u52a0\u81f3", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u914d\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6539\u6b63\u6570", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5f52\u7b97\u81f3", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5408\u5e76", None))
    # retranslateUi

