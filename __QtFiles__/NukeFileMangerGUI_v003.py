# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NukeFileMangerGUI_v003.ui'
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
        self.actionSet_Root_Directory = QAction(MainWindow)
        self.actionSet_Root_Directory.setObjectName(u"actionSet_Root_Directory")
        self.scriptBrowser_centralwidget = QWidget(MainWindow)
        self.scriptBrowser_centralwidget.setObjectName(u"scriptBrowser_centralwidget")
        self.launchNukeIndie_pushButton = QPushButton(self.scriptBrowser_centralwidget)
        self.launchNukeIndie_pushButton.setObjectName(u"launchNukeIndie_pushButton")
        self.launchNukeIndie_pushButton.setGeometry(QRect(160, 690, 184, 33))
        font = QFont()
        font.setPointSize(16)
        self.launchNukeIndie_pushButton.setFont(font)
        self.scripts_listView = QListView(self.scriptBrowser_centralwidget)
        self.scripts_listView.setObjectName(u"scripts_listView")
        self.scripts_listView.setGeometry(QRect(9, 39, 511, 361))
        self.enter_shotinfo_pushButton = QPushButton(self.scriptBrowser_centralwidget)
        self.enter_shotinfo_pushButton.setObjectName(u"enter_shotinfo_pushButton")
        self.enter_shotinfo_pushButton.setGeometry(QRect(220, 530, 181, 31))
        self.rootDir_lineEdit = QLineEdit(self.scriptBrowser_centralwidget)
        self.rootDir_lineEdit.setObjectName(u"rootDir_lineEdit")
        self.rootDir_lineEdit.setGeometry(QRect(110, 410, 401, 31))
        self.rootDir_lineEdit.setAlignment(Qt.AlignCenter)
        self.shotCode_comboBox = QComboBox(self.scriptBrowser_centralwidget)
        self.shotCode_comboBox.setObjectName(u"shotCode_comboBox")
        self.shotCode_comboBox.setGeometry(QRect(110, 490, 401, 31))
        self.shot_label = QLabel(self.scriptBrowser_centralwidget)
        self.shot_label.setObjectName(u"shot_label")
        self.shot_label.setGeometry(QRect(50, 490, 61, 31))
        self.shot_label.setFont(font)
        self.show_label = QLabel(self.scriptBrowser_centralwidget)
        self.show_label.setObjectName(u"show_label")
        self.show_label.setGeometry(QRect(40, 453, 61, 21))
        self.show_label.setFont(font)
        self.Directory_label = QLabel(self.scriptBrowser_centralwidget)
        self.Directory_label.setObjectName(u"Directory_label")
        self.Directory_label.setGeometry(QRect(10, 413, 91, 21))
        self.Directory_label.setFont(font)
        self.showCode_comboBox = QComboBox(self.scriptBrowser_centralwidget)
        self.showCode_comboBox.setObjectName(u"showCode_comboBox")
        self.showCode_comboBox.setGeometry(QRect(110, 450, 401, 31))
        self.tabWidget = QTabWidget(self.scriptBrowser_centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, -2, 531, 29))
        font1 = QFont()
        font1.setPointSize(12)
        self.tabWidget.setFont(font1)
        self.scriptBrowser_tab = QWidget()
        self.scriptBrowser_tab.setObjectName(u"scriptBrowser_tab")
        self.tabWidget.addTab(self.scriptBrowser_tab, "")
        self.showBuilder_tab = QWidget()
        self.showBuilder_tab.setObjectName(u"showBuilder_tab")
        self.tabWidget.addTab(self.showBuilder_tab, "")
        self.shotBuilder_tab = QWidget()
        self.shotBuilder_tab.setObjectName(u"shotBuilder_tab")
        self.tabWidget.addTab(self.shotBuilder_tab, "")
        MainWindow.setCentralWidget(self.scriptBrowser_centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 532, 21))
        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file_menu.menuAction())
        self.file_menu.addAction(self.actionSet_Root_Directory)
        self.file_menu.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSet_Root_Directory.setText(QCoreApplication.translate("MainWindow", u"Set Root Directory", None))
        self.launchNukeIndie_pushButton.setText(QCoreApplication.translate("MainWindow", u"Launch Nuke Indie", None))
        self.enter_shotinfo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Update Shot List", None))
        self.rootDir_lineEdit.setInputMask("")
        self.rootDir_lineEdit.setText("")
        self.rootDir_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Root Directory", None))
        self.shot_label.setText(QCoreApplication.translate("MainWindow", u"Shot: ", None))
        self.show_label.setText(QCoreApplication.translate("MainWindow", u"Show:", None))
        self.Directory_label.setText(QCoreApplication.translate("MainWindow", u"Directory:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scriptBrowser_tab), QCoreApplication.translate("MainWindow", u"Script Browser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.showBuilder_tab), QCoreApplication.translate("MainWindow", u"Show Builder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shotBuilder_tab), QCoreApplication.translate("MainWindow", u"Shot Builder", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

