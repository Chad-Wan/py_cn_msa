# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dxf_analysis_and_creation_ui.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(739, 508)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.comboBox_output_format_gp1 = QComboBox(self.groupBox)
        self.comboBox_output_format_gp1.setObjectName(u"comboBox_output_format_gp1")

        self.gridLayout.addWidget(self.comboBox_output_format_gp1, 4, 1, 1, 1)

        self.pushButton_browser_to_dxf_gp1 = QPushButton(self.groupBox)
        self.pushButton_browser_to_dxf_gp1.setObjectName(u"pushButton_browser_to_dxf_gp1")
        self.pushButton_browser_to_dxf_gp1.setFont(font)
        self.pushButton_browser_to_dxf_gp1.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_browser_to_dxf_gp1, 0, 2, 1, 1)

        self.lineEdit_dxf_path_gp1 = QLineEdit(self.groupBox)
        self.lineEdit_dxf_path_gp1.setObjectName(u"lineEdit_dxf_path_gp1")
        self.lineEdit_dxf_path_gp1.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_dxf_path_gp1, 0, 1, 1, 1)

        self.lineEdit_output_path_gp1 = QLineEdit(self.groupBox)
        self.lineEdit_output_path_gp1.setObjectName(u"lineEdit_output_path_gp1")
        self.lineEdit_output_path_gp1.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_output_path_gp1, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_target_layer_gp1 = QLineEdit(self.groupBox)
        self.lineEdit_target_layer_gp1.setObjectName(u"lineEdit_target_layer_gp1")
        self.lineEdit_target_layer_gp1.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_target_layer_gp1, 1, 1, 1, 1)

        self.pushButton_browser_to_output_path_gp1 = QPushButton(self.groupBox)
        self.pushButton_browser_to_output_path_gp1.setObjectName(u"pushButton_browser_to_output_path_gp1")
        self.pushButton_browser_to_output_path_gp1.setFont(font)
        self.pushButton_browser_to_output_path_gp1.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_browser_to_output_path_gp1, 2, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_start_output_pg1 = QPushButton(self.groupBox)
        self.pushButton_start_output_pg1.setObjectName(u"pushButton_start_output_pg1")
        self.pushButton_start_output_pg1.setFont(font)
        self.pushButton_start_output_pg1.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_start_output_pg1, 4, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEdit_target_layer_gp2 = QLineEdit(self.groupBox_2)
        self.lineEdit_target_layer_gp2.setObjectName(u"lineEdit_target_layer_gp2")
        self.lineEdit_target_layer_gp2.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_target_layer_gp2, 2, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.pushButton_browser_to_output_path_gp2 = QPushButton(self.groupBox_2)
        self.pushButton_browser_to_output_path_gp2.setObjectName(u"pushButton_browser_to_output_path_gp2")
        self.pushButton_browser_to_output_path_gp2.setFont(font)
        self.pushButton_browser_to_output_path_gp2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.pushButton_browser_to_output_path_gp2, 3, 2, 1, 1)

        self.pushButton_start_output_gp2 = QPushButton(self.groupBox_2)
        self.pushButton_start_output_gp2.setObjectName(u"pushButton_start_output_gp2")
        self.pushButton_start_output_gp2.setFont(font)
        self.pushButton_start_output_gp2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.pushButton_start_output_gp2, 5, 2, 1, 1)

        self.lineEdit_csv_path_gp2 = QLineEdit(self.groupBox_2)
        self.lineEdit_csv_path_gp2.setObjectName(u"lineEdit_csv_path_gp2")
        self.lineEdit_csv_path_gp2.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_csv_path_gp2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.lineEdit_output_path_gp2 = QLineEdit(self.groupBox_2)
        self.lineEdit_output_path_gp2.setObjectName(u"lineEdit_output_path_gp2")
        self.lineEdit_output_path_gp2.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_output_path_gp2, 3, 1, 1, 1)

        self.pushButton_browser_to_csv_gp2 = QPushButton(self.groupBox_2)
        self.pushButton_browser_to_csv_gp2.setObjectName(u"pushButton_browser_to_csv_gp2")
        self.pushButton_browser_to_csv_gp2.setFont(font)
        self.pushButton_browser_to_csv_gp2.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.pushButton_browser_to_csv_gp2, 1, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 2)

        self.comboBox_remove_duplication_gp2 = QComboBox(self.groupBox_2)
        self.comboBox_remove_duplication_gp2.setObjectName(u"comboBox_remove_duplication_gp2")

        self.gridLayout_2.addWidget(self.comboBox_remove_duplication_gp2, 5, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"dxf analysis and creation", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5c06dxf\u67d0\u5c42\u4e2d\u7684\u6298\u7ebf\u5bfc\u51fa\uff08\u5305\u542b\u6bcf\u6761\u7ebf\u7684\u8d77\u70b9\uff0c\u6298\u70b9\uff0c\u7ec8\u70b9\uff09", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u683c\u5f0f\uff1a", None))
        self.comboBox_output_format_gp1.setCurrentText("")
        self.comboBox_output_format_gp1.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u5bfc\u51fa\u683c\u5f0f", None))
        self.pushButton_browser_to_dxf_gp1.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u8def\u5f84\uff1a", None))
        self.pushButton_browser_to_output_path_gp1.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u56fe\u5c42\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6e90dxf\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.pushButton_start_output_pg1.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5bfc\u51fa", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u6839\u636e\u5df2\u77e5\u70b9\u5750\u6807\u548c\u6807\u53f7\uff0c\u751f\u6210\u4e00\u4e2adxf\u6587\u4ef6", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u8def\u5f84\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5df2\u77e5\u70b9csv\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.pushButton_browser_to_output_path_gp2.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.pushButton_start_output_gp2.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5bfc\u51fa", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u56fe\u5c42\uff1a", None))
        self.pushButton_browser_to_csv_gp2.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Note: \u5df2\u77e5\u70b9\u5750\u6807\u5bfc\u5165\u683c\u5f0f\u8bf7\u53c2\u7167\u4e0a\u6a21\u5757\u4e00\u751f\u6210\u7684cvs\u6587\u4ef6\uff08\u6bcf\u884c\u683c\u5f0f\u4e3a\uff1a\u6807\u53f7 x\u5750\u6807 y\u5750\u6807\uff09", None))
        self.comboBox_remove_duplication_gp2.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u53bb\u9664\u91cd\u590d\u70b9\uff1f", None))
    # retranslateUi

