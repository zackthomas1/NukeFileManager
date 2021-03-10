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
        self.showCode_lineEdit.setGeometry(QRect(110, 420, 401, 31))
        self.showCode_lineEdit.setAlignment(Qt.AlignCenter)
        self.enter_shotinfo_pushButton = QPushButton(self.centralwidget)
        self.enter_shotinfo_pushButton.setObjectName(u"enter_shotinfo_pushButton")
        self.enter_shotinfo_pushButton.setGeometry(QRect(170, 510, 181, 31))
        self.rootDir_lineEdit = QLineEdit(self.centralwidget)
        self.rootDir_lineEdit.setObjectName(u"rootDir_lineEdit")
        self.rootDir_lineEdit.setGeometry(QRect(110, 380, 401, 31))
        self.rootDir_lineEdit.setAlignment(Qt.AlignCenter)
        self.shotCode_comboBox = QComboBox(self.centralwidget)
        self.shotCode_comboBox.setObjectName(u"shotCode_comboBox")
        self.shotCode_comboBox.setGeometry(QRect(110, 460, 401, 31))
        self.Shot_label = QLabel(self.centralwidget)
        self.Shot_label.setObjectName(u"Shot_label")
        self.Shot_label.setGeometry(QRect(50, 460, 61, 31))
        self.Shot_label.setFont(font)
        self.Show_label = QLabel(self.centralwidget)
        self.Show_label.setObjectName(u"Show_label")
        self.Show_label.setGeometry(QRect(40, 423, 61, 21))
        self.Show_label.setFont(font)
        self.Directory_label = QLabel(self.centralwidget)
        self.Directory_label.setObjectName(u"Directory_label")
        self.Directory_label.setGeometry(QRect(10, 383, 91, 21))
        self.Directory_label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 532, 21))
        self.menuShot_Browser = QMenu(self.menubar)
        self.menuShot_Browser.setObjectName(u"menuShot_Browser")
        self.menuShow_Builder = QMenu(self.menubar)
        self.menuShow_Builder.setObjectName(u"menuShow_Builder")
        self.menuShot_Builder = QMenu(self.menubar)
        self.menuShot_Builder.setObjectName(u"menuShot_Builder")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuShot_Browser.menuAction())
        self.menubar.addAction(self.menuShow_Builder.menuAction())
        self.menubar.addAction(self.menuShot_Builder.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.launchNukeIndie_pushButton.setText(QCoreApplication.translate("MainWindow", u"Launch Nuke Indie", None))
        self.showCode_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Show Code", None))
        self.enter_shotinfo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Update Shot List", None))
        self.rootDir_lineEdit.setInputMask("")
        self.rootDir_lineEdit.setText("")
        self.rootDir_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Root Directory", None))
        self.Shot_label.setText(QCoreApplication.translate("MainWindow", u"Shot: ", None))
        self.Show_label.setText(QCoreApplication.translate("MainWindow", u"Show:", None))
        self.Directory_label.setText(QCoreApplication.translate("MainWindow", u"Directory:", None))
        self.menuShot_Browser.setTitle(QCoreApplication.translate("MainWindow", u"Shot Browser", None))
        self.menuShow_Builder.setTitle(QCoreApplication.translate("MainWindow", u"Show Builder", None))
        self.menuShot_Builder.setTitle(QCoreApplication.translate("MainWindow", u"Shot Builder", None))
    # retranslateUi

