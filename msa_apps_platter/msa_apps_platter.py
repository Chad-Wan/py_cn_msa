# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'msa_apps_platter.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 722)
        self.action_about_this_app = QAction(MainWindow)
        self.action_about_this_app.setObjectName(u"action_about_this_app")
        font = QFont()
        font.setPointSize(13)
        self.action_about_this_app.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setFamilies([u"Adwaita Sans"])
        font1.setPointSize(16)
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, -1, 10, -1)
        self.pushButton_leveling_record_and_check = QPushButton(self.groupBox)
        self.pushButton_leveling_record_and_check.setObjectName(u"pushButton_leveling_record_and_check")
        self.pushButton_leveling_record_and_check.setEnabled(False)
        self.pushButton_leveling_record_and_check.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
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

        self.verticalLayout_4.addWidget(self.pushButton_leveling_record_and_check)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.pushButton_xtf_to_dxf_track_line = QPushButton(self.groupBox_3)
        self.pushButton_xtf_to_dxf_track_line.setObjectName(u"pushButton_xtf_to_dxf_track_line")
        self.pushButton_xtf_to_dxf_track_line.setEnabled(False)
        self.pushButton_xtf_to_dxf_track_line.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
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

        self.verticalLayout_2.addWidget(self.pushButton_xtf_to_dxf_track_line)

        self.pushButton_xtf_to_recording = QPushButton(self.groupBox_3)
        self.pushButton_xtf_to_recording.setObjectName(u"pushButton_xtf_to_recording")
        self.pushButton_xtf_to_recording.setEnabled(True)
        self.pushButton_xtf_to_recording.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.pushButton_xtf_to_recording)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.pushButton_caris_time_converter = QPushButton(self.groupBox_2)
        self.pushButton_caris_time_converter.setObjectName(u"pushButton_caris_time_converter")
        self.pushButton_caris_time_converter.setEnabled(True)
        self.pushButton_caris_time_converter.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton_caris_time_converter)

        self.pushButton_hvf_editor = QPushButton(self.groupBox_2)
        self.pushButton_hvf_editor.setObjectName(u"pushButton_hvf_editor")
        self.pushButton_hvf_editor.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton_hvf_editor)

        self.pushButton_hvf_editor_2 = QPushButton(self.groupBox_2)
        self.pushButton_hvf_editor_2.setObjectName(u"pushButton_hvf_editor_2")
        self.pushButton_hvf_editor_2.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton_hvf_editor_2)

        self.pushButton_hvf_editor_3 = QPushButton(self.groupBox_2)
        self.pushButton_hvf_editor_3.setObjectName(u"pushButton_hvf_editor_3")
        self.pushButton_hvf_editor_3.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton_hvf_editor_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font1)
        self.groupBox_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.pushButton_water_level_record = QPushButton(self.groupBox_4)
        self.pushButton_water_level_record.setObjectName(u"pushButton_water_level_record")
        self.pushButton_water_level_record.setEnabled(False)
        self.pushButton_water_level_record.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
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

        self.verticalLayout_3.addWidget(self.pushButton_water_level_record)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font1)
        self.groupBox_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, -1, 10, -1)
        self.pushButton_dxf_ana_and_gen = QPushButton(self.groupBox_5)
        self.pushButton_dxf_ana_and_gen.setObjectName(u"pushButton_dxf_ana_and_gen")
        self.pushButton_dxf_ana_and_gen.setEnabled(True)
        self.pushButton_dxf_ana_and_gen.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
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

        self.verticalLayout_5.addWidget(self.pushButton_dxf_ana_and_gen)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)


        self.gridLayout.addWidget(self.groupBox_5, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_about_this_app)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6d77\u6d4b\u5de5\u5177\u7bb1 -- by Mr. Wan", None))
        self.action_about_this_app.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u5de5\u5177\u7684\u8bf4\u660e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6c34\u51c6\u5de5\u5177", None))
        self.pushButton_leveling_record_and_check.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u51c6\u6d4b\u91cf\n"
"\u8bb0\u5f55/\u68c0\u67e5\u5de5\u5177", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"xtf\u5de5\u5177", None))
        self.pushButton_xtf_to_dxf_track_line.setText(QCoreApplication.translate("MainWindow", u"\u4ecextf\u5bfc\u51fadxf\u822a\u8ff9", None))
        self.pushButton_xtf_to_recording.setText(QCoreApplication.translate("MainWindow", u"\u4ecextf\u5bfc\u51fa\u5916\u4e1a\n"
"\u6570\u636e\u91c7\u96c6\u8bb0\u5f55\u8868", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"CARIS\u5de5\u5177", None))
        self.pushButton_caris_time_converter.setText(QCoreApplication.translate("MainWindow", u"CARIS\u65f6\u95f4\n"
"\u8f6c\u6362\u5de5\u5177", None))
        self.pushButton_hvf_editor.setText(QCoreApplication.translate("MainWindow", u"hvf\u8f85\u52a9\u7f16\u8f91\u5de5\u5177", None))
        self.pushButton_hvf_editor_2.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u52a0\u81f3\u6f6e\u4f4d\u6587\u4ef6(tid)", None))
        self.pushButton_hvf_editor_3.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u52a0\u81f3\u58f0\u901f\u6587\u4ef6(svp)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"MISC", None))
        self.pushButton_water_level_record.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u4f4d\u89c2\u5bdf\u8bb0\u5f55", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"CAD", None))
        self.pushButton_dxf_ana_and_gen.setText(QCoreApplication.translate("MainWindow", u"dxf\u5bfc\u51fa\u67d0\u56fe\u5c42\u6298\u7ebf", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"README", None))
    # retranslateUi

