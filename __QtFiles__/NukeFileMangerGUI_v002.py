# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NukeFileMangerGUI_v002.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        MainWindow.resize(532, 766)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.launchNukeIndie_pushButton = QPushButton(self.centralwidget)
        self.launchNukeIndie_pushButton.setObjectName(u"launchNukeIndie_pushButton")
        self.launchNukeIndie_pushButton.setGeometry(QRect(160, 690, 184, 33))
        font = QFont()
        font.setPointSize(16)
        self.launchNukeIndie_pushButton.setFont(font)
        self.nkFiles_listView = QListView(self.centralwidget)
        self.nkFiles_listView.setObjectName(u"nkFiles_listView")
        self.nkFiles_listView.setGeometry(QRect(9, 9, 511, 361))
        self.showCode_lineEdit = QLineEdit(self.centralwidget)
        self.showCode_lineEdit.setObjectName(u"showCode_lineEdit")
        self.showCode_lineEdit.setGeometry(QRect(10, 420, 501, 31))
        self.showCode_lineEdit.setAlignment(Qt.AlignCenter)
        self.shotCode_lineEdit = QLineEdit(self.centralwidget)
        self.shotCode_lineEdit.setObjectName(u"shotCode_lineEdit")
        self.shotCode_lineEdit.setGeometry(QRect(10, 460, 501, 31))
        self.shotCode_lineEdit.setAlignment(Qt.AlignCenter)
        self.enter_shotinfo_pushButton = QPushButton(self.centralwidget)
        self.enter_shotinfo_pushButton.setObjectName(u"enter_shotinfo_pushButton")
        self.enter_shotinfo_pushButton.setGeometry(QRect(160, 650, 181, 31))
        self.rootDir_lineEdit = QLineEdit(self.centralwidget)
        self.rootDir_lineEdit.setObjectName(u"rootDir_lineEdit")
        self.rootDir_lineEdit.setGeometry(QRect(10, 380, 501, 31))
        self.rootDir_lineEdit.setAlignment(Qt.AlignCenter)
        self.shotCode_comboBox = QComboBox(self.centralwidget)
        self.shotCode_comboBox.setObjectName(u"shotCode_comboBox")
        self.shotCode_comboBox.setGeometry(QRect(10, 500, 491, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 532, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.launchNukeIndie_pushButton.setText(QCoreApplication.translate("MainWindow", u"Launch Nuke Indie", None))
        self.showCode_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Show Code", None))
        self.shotCode_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Shot Number", None))
        self.enter_shotinfo_pushButton.setText(QCoreApplication.translate("MainWindow", u"enter shot info", None))
        self.rootDir_lineEdit.setInputMask("")
        self.rootDir_lineEdit.setText("")
        self.rootDir_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Root Directory", None))
    # retranslateUi

