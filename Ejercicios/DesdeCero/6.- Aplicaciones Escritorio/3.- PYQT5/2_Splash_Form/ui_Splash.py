# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Splashpfykyo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(604, 300)
        MainWindow.setStyleSheet(u"background:#1c1c1c;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.DropShadowFrame = QFrame(self.centralwidget)
        self.DropShadowFrame.setObjectName(u"DropShadowFrame")
        self.DropShadowFrame.setStyleSheet(u"QFrame {\n"
"    background-color:rgb(56, 58, 89);\n"
"	color:rgb(216, 246, 255);\n"
"}")
        self.DropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.DropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 20, 581, 71))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(245, 102, 255);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_Description = QLabel(self.DropShadowFrame)
        self.label_Description.setObjectName(u"label_Description")
        self.label_Description.setGeometry(QRect(0, 80, 581, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_Description.setFont(font1)
        self.label_Description.setStyleSheet(u"color: rgb(219, 255, 255);")
        self.label_Description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.DropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 170, 541, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(124, 129, 198);\n"
"	color: rgb(170, 255, 255);\n"
"	border-style:none;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 18, 255, 255), stop:0.983051 rgba(122, 126, 191, 255), stop:1 rgba(255, 253, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.DropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 190, 581, 31))
        self.label_loading.setFont(font1)
        self.label_loading.setStyleSheet(u"color: rgb(219, 255, 255);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.DropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(0, 250, 581, 31))
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: rgb(219, 255, 255);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.DropShadowFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<strong>YOUR</strong> APP NAME", None))
        self.label_Description.setText(QCoreApplication.translate("MainWindow", u"<strong>APP</strong> DESCRIPTION", None))
        self.label_loading.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Loading....</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:7pt; font-weight:600;\">Created by:</span><span style=\" font-size:10pt;\"> Javier Esteban</span></p></body></html>", None))
    # retranslateUi

