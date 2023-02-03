# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_1.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(808, 616)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(24,24,24);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"background-color:rgb(17, 17, 17);\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:10px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(44, 44, 44);\n"
"}\n"
"\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(583, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_min = QPushButton(self.frame_superior)
        self.bt_min.setObjectName(u"bt_min")
        self.bt_min.setMinimumSize(QSize(38, 40))
        self.bt_min.setMaximumSize(QSize(38, 40))
        self.bt_min.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_min.setFocusPolicy(Qt.WheelFocus)
        self.bt_min.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u"img/mini.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_min.setIcon(icon)
        self.bt_min.setIconSize(QSize(45, 38))
        self.bt_min.setCheckable(False)
        self.bt_min.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.bt_min)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMinimumSize(QSize(38, 38))
        self.bt_cerrar.setMaximumSize(QSize(38, 38))
        self.bt_cerrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cerrar.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"img/close-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon1)
        self.bt_cerrar.setIconSize(QSize(45, 38))

        self.horizontalLayout.addWidget(self.bt_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border-radius: 120px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgb(0,0,0);\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 70, 281, 161))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font: 87 12pt \"Arial-Black\";")

        self.horizontalLayout_3.addWidget(self.label)

        self.cb_puertoSerial = QComboBox(self.layoutWidget)
        self.cb_puertoSerial.setObjectName(u"cb_puertoSerial")
        self.cb_puertoSerial.setStyleSheet(u"QComboBox {\n"
"border: 3px solid #111111;\n"
"border-radius: 5px;\n"
"min-width: 6em;\n"
"color: rgb(25, 0, 175);\n"
"font: 87 12pt \"Arial Black\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 15px;\n"
"border-left-width: 3px;\n"
"border-left-color: #111111;\n"
"border-left-style: solid;\n"
"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"background: #2c2c2c;\n"
"selection-background-color: rgb(25, 0, 175);\n"
"color: #111111;\n"
"}")

        self.horizontalLayout_3.addWidget(self.cb_puertoSerial)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: white;\n"
"font: 87 12pt \"Arial-Black\";")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.cb_baudrates = QComboBox(self.layoutWidget)
        self.cb_baudrates.setObjectName(u"cb_baudrates")
        self.cb_baudrates.setStyleSheet(u"QComboBox {\n"
"border: 3px solid #111111;\n"
"border-radius: 5px;\n"
"min-width: 6em;\n"
"color: rgb(25, 0, 175);\n"
"font: 87 12pt \"Arial Black\";\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 15px;\n"
"border-left-width: 3px;\n"
"border-left-color: #111111;\n"
"border-left-style: solid;\n"
"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"background: #2c2c2c;\n"
"selection-background-color: rgb(25, 0, 175);\n"
"color: #111111;\n"
"}")

        self.horizontalLayout_4.addWidget(self.cb_baudrates)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bt_connect = QPushButton(self.layoutWidget)
        self.bt_connect.setObjectName(u"bt_connect")
        self.bt_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_connect.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(25, 0, 175);\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(25, 0, 175);\n"
"}")

        self.horizontalLayout_5.addWidget(self.bt_connect)

        self.bt_disconnect = QPushButton(self.layoutWidget)
        self.bt_disconnect.setObjectName(u"bt_disconnect")
        self.bt_disconnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_disconnect.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(25, 0, 175);\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(25, 0, 175);\n"
"}")

        self.horizontalLayout_5.addWidget(self.bt_disconnect)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.bt_update = QPushButton(self.layoutWidget)
        self.bt_update.setObjectName(u"bt_update")
        self.bt_update.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_update.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(25, 0, 175);\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"color: rgb(25, 0, 175);\n"
"}")

        self.verticalLayout_7.addWidget(self.bt_update)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 10, 71, 61))
        self.label_7.setPixmap(QPixmap(u"img/bmw.png"))
        self.label_7.setScaledContents(True)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(260, 30, 41, 31))
        self.label_12.setPixmap(QPixmap(u"img/abs.jpg"))
        self.label_12.setScaledContents(True)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(80, 30, 51, 31))
        self.label_11.setPixmap(QPixmap(u"img/Check-engine.jpg"))
        self.label_11.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color:rgb(0,0,0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.frame_5)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(60, 30, 251, 42))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.direcc_izq = QRadioButton(self.layoutWidget_2)
        self.direcc_izq.setObjectName(u"direcc_izq")
        self.direcc_izq.setStyleSheet(u"QRadioButton {\n"
"color: white;\n"
"font: 87 12pt \"Arial-Black\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 45px;\n"
"height: 	30px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"background-color: #00ff00;\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"background-color: rgb(0,130,0);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"\n"
"")
        self.direcc_izq.setCheckable(True)
        self.direcc_izq.setChecked(False)
        self.direcc_izq.setAutoExclusive(False)

        self.horizontalLayout_12.addWidget(self.direcc_izq)

        self.direcc_der = QRadioButton(self.layoutWidget_2)
        self.direcc_der.setObjectName(u"direcc_der")
        self.direcc_der.setStyleSheet(u"QRadioButton {\n"
"color: white;\n"
"font: 87 12pt \"Arial-Black\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 45px;\n"
"height: 	30px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"background-color: #00ff00;\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"background-color: rgb(0,130,0);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"")
        self.direcc_der.setAutoExclusive(False)

        self.horizontalLayout_12.addWidget(self.direcc_der)

        self.layoutWidget_3 = QWidget(self.frame_5)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(90, 160, 251, 42))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.test_gas = QRadioButton(self.layoutWidget_3)
        self.test_gas.setObjectName(u"test_gas")
        self.test_gas.setStyleSheet(u"QRadioButton {\n"
"color: white;\n"
"font: 87 12pt \"Arial-Black\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 45px;\n"
"height: 	30px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"background-color: rgb(250,150,0);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"background-color: rgb(255,200,0);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"")
        self.test_gas.setCheckable(True)
        self.test_gas.setChecked(False)
        self.test_gas.setAutoExclusive(False)

        self.horizontalLayout_13.addWidget(self.test_gas)

        self.test_door = QRadioButton(self.layoutWidget_3)
        self.test_door.setObjectName(u"test_door")
        self.test_door.setStyleSheet(u"QRadioButton {\n"
"color: white;\n"
"font: 87 12pt \"Arial-Black\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 45px;\n"
"height: 	30px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"background-color: rgb(150,255,255);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"background-color: rgb(100,100,100);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"")
        self.test_door.setAutoExclusive(False)

        self.horizontalLayout_13.addWidget(self.test_door)

        self.slider_gas = QSlider(self.frame_5)
        self.slider_gas.setObjectName(u"slider_gas")
        self.slider_gas.setGeometry(QRect(70, 220, 101, 16))
        self.slider_gas.setLayoutDirection(Qt.RightToLeft)
        self.slider_gas.setStyleSheet(u"QSlider::groove:horizontal {\n"
"	border: 1px solid white;\n"
"	height: 4px;\n"
"	background:rgb(255,200,0);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	background: rgb(255,200,0);\n"
"	width: 28px;\n"
"	height: 28px;\n"
"\n"
"left: 11px;\n"
"right: 11px;\n"
"\n"
"	margin: -12px;\n"
"	border-radius: 14px;\n"
"\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"background-color: white;\n"
"border: 1px solid white;\n"
"}")
        self.slider_gas.setOrientation(Qt.Horizontal)
        self.layoutWidget1 = QWidget(self.frame_5)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 90, 341, 44))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stop1 = QRadioButton(self.layoutWidget1)
        self.stop1.setObjectName(u"stop1")
        self.stop1.setStyleSheet(u"QRadioButton {\n"
"color: white;\n"
"font: 87 12pt \"Arial-Black\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 25px;\n"
"height: 	20px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"background-color: #00ff00;\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"background-color: rgb(0,130,0);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"\n"
"")
        self.stop1.setCheckable(True)
        self.stop1.setChecked(False)
        self.stop1.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.stop1)

        self.stop2 = QRadioButton(self.layoutWidget1)
        self.stop2.setObjectName(u"stop2")
        self.stop2.setStyleSheet(u"QRadioButton {\n"
"color: white;\n"
"font: 87 12pt \"Arial-Black\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 25px;\n"
"height: 	20px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"background-color: #00ff00;\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"background-color: rgb(0,130,0);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"\n"
"")
        self.stop2.setCheckable(True)
        self.stop2.setChecked(False)
        self.stop2.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.stop2)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.value_luces = QLabel(self.layoutWidget1)
        self.value_luces.setObjectName(u"value_luces")
        self.value_luces.setLayoutDirection(Qt.RightToLeft)
        self.value_luces.setStyleSheet(u"color: white;\n"
"font: 87 8pt \"Arial-Black\";")
        self.value_luces.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.value_luces)

        self.test_luces = QRadioButton(self.layoutWidget1)
        self.test_luces.setObjectName(u"test_luces")
        self.test_luces.setStyleSheet(u"QRadioButton {\n"
"color: white;\n"
"font: 87 12pt \"Arial-Black\";\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 45px;\n"
"height: 	30px;\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"background-color: rgb(225, 255, 25);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"background-color: rgb(218, 255, 195);\n"
"border: 5px solid #111111;\n"
"}\n"
"\n"
"")
        self.test_luces.setAutoExclusive(False)

        self.horizontalLayout_7.addWidget(self.test_luces)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_7)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 160, 51, 31))
        self.label_9.setPixmap(QPixmap(u"img/testigo-gasolina-300x169.jpg"))
        self.label_9.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color:rgb(0,0,0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.layoutWidget2 = QWidget(self.frame_4)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 100, 281, 131))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: white;\n"
"font: 87 12pt \"Arial-Black\";")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.vel_lcd = QLCDNumber(self.layoutWidget2)
        self.vel_lcd.setObjectName(u"vel_lcd")
        self.vel_lcd.setMinimumSize(QSize(0, 0))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(33, 102, 204, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        brush2 = QBrush(QColor(25, 28, 160, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.vel_lcd.setPalette(palette)
        self.vel_lcd.setDigitCount(7)
        self.vel_lcd.setProperty("intValue", 0)

        self.horizontalLayout_8.addWidget(self.vel_lcd)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: white;\n"
"font: 87 12pt \"Arial-Black\";")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.rpm_lcd = QLCDNumber(self.layoutWidget2)
        self.rpm_lcd.setObjectName(u"rpm_lcd")
        self.rpm_lcd.setMinimumSize(QSize(0, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.rpm_lcd.setPalette(palette1)
        self.rpm_lcd.setDigitCount(7)
        self.rpm_lcd.setProperty("intValue", 0)

        self.horizontalLayout_9.addWidget(self.rpm_lcd)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(110, 10, 171, 91))
        self.label_13.setPixmap(QPixmap(u"img/tablero-instrumentos-coche-velocimetro-tacometro-odometro-temperatura-sensor-combustible-ilustracion-vectorial_131573-6.png"))
        self.label_13.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color:rgb(0,0,0);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.layoutWidget3 = QWidget(self.frame_6)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(40, 60, 301, 161))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_3 = QLabel(self.layoutWidget3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: white;\n"
"font: 87 12pt \"Arial-Black\";")

        self.horizontalLayout_11.addWidget(self.label_3)

        self.temp_lcd = QLCDNumber(self.layoutWidget3)
        self.temp_lcd.setObjectName(u"temp_lcd")
        self.temp_lcd.setMinimumSize(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.temp_lcd.setPalette(palette2)
        self.temp_lcd.setDigitCount(7)
        self.temp_lcd.setProperty("intValue", 0)

        self.horizontalLayout_11.addWidget(self.temp_lcd)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.layoutWidget3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: white;\n"
"font: 87 12pt \"Arial-Black\";")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.km_lcd = QLCDNumber(self.layoutWidget3)
        self.km_lcd.setObjectName(u"km_lcd")
        self.km_lcd.setMinimumSize(QSize(0, 0))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.km_lcd.setPalette(palette3)
        self.km_lcd.setDigitCount(7)
        self.km_lcd.setProperty("intValue", 0)

        self.horizontalLayout_10.addWidget(self.km_lcd)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 20, 51, 31))
        self.label_8.setPixmap(QPixmap(u"img/Sensor-de-Temperatura.jpg"))
        self.label_8.setScaledContents(True)
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(200, 10, 61, 41))
        self.label_10.setPixmap(QPixmap(u"img/glow-speedometer-dashboard-260nw-1348889378.png"))
        self.label_10.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_min.setText("")
        self.bt_cerrar.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Puerto:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Baudrate:", None))
        self.bt_connect.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.bt_disconnect.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.bt_update.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.label_7.setText("")
        self.label_12.setText("")
        self.label_11.setText("")
        self.direcc_izq.setText(QCoreApplication.translate("MainWindow", u"IZQ", None))
        self.direcc_der.setText(QCoreApplication.translate("MainWindow", u"DER", None))
        self.test_gas.setText(QCoreApplication.translate("MainWindow", u"GAS", None))
        self.test_door.setText(QCoreApplication.translate("MainWindow", u"DOOR", None))
        self.stop1.setText("")
        self.stop2.setText("")
        self.value_luces.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.test_luces.setText(QCoreApplication.translate("MainWindow", u"LUCES", None))
        self.label_9.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Velocidad (km/h):", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"RPM:", None))
        self.label_13.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Temperatura (\u00b0C):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Contador KM:", None))
        self.label_8.setText("")
        self.label_10.setText("")
    # retranslateUi

