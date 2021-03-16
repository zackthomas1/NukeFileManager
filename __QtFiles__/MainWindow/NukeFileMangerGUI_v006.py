# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NukeFileMangerGUI_v006.ui'
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
        MainWindow.resize(550, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.openSettings_action = QAction(MainWindow)
        self.openSettings_action.setObjectName(u"openSettings_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, -2, 531, 29))
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.scriptBrowser_tab = QWidget()
        self.scriptBrowser_tab.setObjectName(u"scriptBrowser_tab")
        self.tabWidget.addTab(self.scriptBrowser_tab, "")
        self.shotBuilder_tab = QWidget()
        self.shotBuilder_tab.setObjectName(u"shotBuilder_tab")
        self.tabWidget.addTab(self.shotBuilder_tab, "")
        self.showBuilder_tab = QWidget()
        self.showBuilder_tab.setObjectName(u"showBuilder_tab")
        self.tabWidget.addTab(self.showBuilder_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 550, 21))
        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file_menu.menuAction())
        self.file_menu.addAction(self.openSettings_action)
        self.file_menu.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openSettings_action.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scriptBrowser_tab), QCoreApplication.translate("MainWindow", u"Script Browser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shotBuilder_tab), QCoreApplication.translate("MainWindow", u"Shot Builder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.showBuilder_tab), QCoreApplication.translate("MainWindow", u"Show Builder", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

