# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'caris_time_converter_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(790, 338)
        font = QFont()
        font.setFamilies([u"Adwaita Sans"])
        font.setPointSize(14)
        Form.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 50, 729, 226))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(60)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox_year_to_conv_upper = QComboBox(self.groupBox)
        self.comboBox_year_to_conv_upper.setObjectName(u"comboBox_year_to_conv_upper")
        self.comboBox_year_to_conv_upper.setEditable(False)

        self.horizontalLayout.addWidget(self.comboBox_year_to_conv_upper)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox_day_to_conv_upper = QSpinBox(self.groupBox)
        self.spinBox_day_to_conv_upper.setObjectName(u"spinBox_day_to_conv_upper")
        self.spinBox_day_to_conv_upper.setMinimum(1)
        self.spinBox_day_to_conv_upper.setMaximum(366)

        self.horizontalLayout.addWidget(self.spinBox_day_to_conv_upper)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 1)

        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.pushButton_day_to_mmdd = QPushButton(self.groupBox)
        self.pushButton_day_to_mmdd.setObjectName(u"pushButton_day_to_mmdd")
        self.pushButton_day_to_mmdd.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_4.addWidget(self.pushButton_day_to_mmdd)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_conved_year_upper = QLabel(self.groupBox)
        self.label_conved_year_upper.setObjectName(u"label_conved_year_upper")
        self.label_conved_year_upper.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_conved_year_upper)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_conved_month_upper = QLabel(self.groupBox)
        self.label_conved_month_upper.setObjectName(u"label_conved_month_upper")
        self.label_conved_month_upper.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_conved_month_upper)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_conved_day_upper = QLabel(self.groupBox)
        self.label_conved_day_upper.setObjectName(u"label_conved_day_upper")
        self.label_conved_day_upper.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_conved_day_upper)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 3)
        self.horizontalLayout_2.setStretch(4, 2)
        self.horizontalLayout_2.setStretch(5, 3)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.comboBox_year_to_conv_lower = QComboBox(self.groupBox_2)
        self.comboBox_year_to_conv_lower.setObjectName(u"comboBox_year_to_conv_lower")
        self.comboBox_year_to_conv_lower.setEditable(False)

        self.horizontalLayout_9.addWidget(self.comboBox_year_to_conv_lower)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.comboBox_mounth_to_conv_lower = QComboBox(self.groupBox_2)
        self.comboBox_mounth_to_conv_lower.setObjectName(u"comboBox_mounth_to_conv_lower")

        self.horizontalLayout_9.addWidget(self.comboBox_mounth_to_conv_lower)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.spinBox_day_to_conv_lower = QSpinBox(self.groupBox_2)
        self.spinBox_day_to_conv_lower.setObjectName(u"spinBox_day_to_conv_lower")
        self.spinBox_day_to_conv_lower.setMinimum(1)
        self.spinBox_day_to_conv_lower.setMaximum(31)

        self.horizontalLayout_9.addWidget(self.spinBox_day_to_conv_lower)

        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_9.addWidget(self.label_16)

        self.horizontalLayout_9.setStretch(0, 6)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 6)
        self.horizontalLayout_9.setStretch(3, 1)
        self.horizontalLayout_9.setStretch(4, 8)
        self.horizontalLayout_9.setStretch(5, 1)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_9)

        self.pushButton_mmdd_to_day = QPushButton(self.groupBox_2)
        self.pushButton_mmdd_to_day.setObjectName(u"pushButton_mmdd_to_day")
        self.pushButton_mmdd_to_day.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_6.addWidget(self.pushButton_mmdd_to_day)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_conved_year_lower = QLabel(self.groupBox_2)
        self.label_conved_year_lower.setObjectName(u"label_conved_year_lower")
        self.label_conved_year_lower.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_conved_year_lower)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.label_conved_day_lower = QLabel(self.groupBox_2)
        self.label_conved_day_lower.setObjectName(u"label_conved_day_lower")
        self.label_conved_day_lower.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_conved_day_lower)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6.setStretch(0, 7)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 3)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"CARIS\u65f6\u95f4\u8f6c\u6362\u5668 --  by Mr. Wan", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5929\u6570 \u8f6c \u65e5\u671f", None))
        self.comboBox_year_to_conv_upper.setCurrentText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u5e74\u7b2c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5929", None))
        self.pushButton_day_to_mmdd.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
        self.label_conved_year_upper.setText(QCoreApplication.translate("Form", u"XXXX", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5e74", None))
        self.label_conved_month_upper.setText(QCoreApplication.translate("Form", u"XX", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u6708", None))
        self.label_conved_day_upper.setText(QCoreApplication.translate("Form", u"XX", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u65e5", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u65e5\u671f \u8f6c \u5929\u6570", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u5e74", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u6708", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u65e5", None))
        self.pushButton_mmdd_to_day.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
        self.label_conved_year_lower.setText(QCoreApplication.translate("Form", u"XXXX", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u5e74\u7b2c", None))
        self.label_conved_day_lower.setText(QCoreApplication.translate("Form", u"XXX", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u5929", None))
    # retranslateUi

