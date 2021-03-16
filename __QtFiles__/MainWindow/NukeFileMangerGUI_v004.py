# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NukeFileMangerGUI_v004.ui'
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
        self.actionSet_Root_Directory = QAction(MainWindow)
        self.actionSet_Root_Directory.setObjectName(u"actionSet_Root_Directory")
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
        self.showBuilder_tab = QWidget()
        self.showBuilder_tab.setObjectName(u"showBuilder_tab")
        self.tabWidget.addTab(self.showBuilder_tab, "")
        self.shotBuilder_tab = QWidget()
        self.shotBuilder_tab.setObjectName(u"shotBuilder_tab")
        self.tabWidget.addTab(self.shotBuilder_tab, "")
        self.scriptBrowser_widget = QWidget(self.centralwidget)
        self.scriptBrowser_widget.setObjectName(u"scriptBrowser_widget")
        self.scriptBrowser_widget.setGeometry(QRect(0, 20, 550, 800))
        self.scriptBrowser_widget.setCursor(QCursor(Qt.ArrowCursor))
        self.shotCode_comboBox = QComboBox(self.scriptBrowser_widget)
        self.shotCode_comboBox.setObjectName(u"shotCode_comboBox")
        self.shotCode_comboBox.setGeometry(QRect(140, 460, 340, 30))
        self.shotCode_comboBox.setFont(font)
        self.rootDir_lineEdit = QLineEdit(self.scriptBrowser_widget)
        self.rootDir_lineEdit.setObjectName(u"rootDir_lineEdit")
        self.rootDir_lineEdit.setGeometry(QRect(140, 380, 340, 30))
        self.rootDir_lineEdit.setFont(font)
        self.rootDir_lineEdit.setAlignment(Qt.AlignCenter)
        self.showCode_comboBox = QComboBox(self.scriptBrowser_widget)
        self.showCode_comboBox.setObjectName(u"showCode_comboBox")
        self.showCode_comboBox.setGeometry(QRect(140, 420, 340, 30))
        self.showCode_comboBox.setFont(font)
        self.updateScriptsList_pushButton = QPushButton(self.scriptBrowser_widget)
        self.updateScriptsList_pushButton.setObjectName(u"updateScriptsList_pushButton")
        self.updateScriptsList_pushButton.setGeometry(QRect(210, 500, 181, 31))
        self.updateScriptsList_pushButton.setFont(font)
        self.launchNukeIndie_pushButton = QPushButton(self.scriptBrowser_widget)
        self.launchNukeIndie_pushButton.setObjectName(u"launchNukeIndie_pushButton")
        self.launchNukeIndie_pushButton.setGeometry(QRect(200, 690, 201, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.launchNukeIndie_pushButton.setFont(font1)
        self.scripts_listView = QListView(self.scriptBrowser_widget)
        self.scripts_listView.setObjectName(u"scripts_listView")
        self.scripts_listView.setGeometry(QRect(20, 10, 511, 341))
        self.scripts_listView.setFont(font)
        self.scripts_listView.setTextElideMode(Qt.ElideMiddle)
        self.scripts_listView.setMovement(QListView.Free)
        self.Directory_label = QLabel(self.scriptBrowser_widget)
        self.Directory_label.setObjectName(u"Directory_label")
        self.Directory_label.setGeometry(QRect(30, 380, 91, 25))
        self.Directory_label.setFont(font1)
        self.show_label = QLabel(self.scriptBrowser_widget)
        self.show_label.setObjectName(u"show_label")
        self.show_label.setGeometry(QRect(60, 420, 58, 25))
        self.show_label.setFont(font1)
        self.shot_label = QLabel(self.scriptBrowser_widget)
        self.shot_label.setObjectName(u"shot_label")
        self.shot_label.setGeometry(QRect(70, 460, 51, 25))
        self.shot_label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.scriptBrowser_widget.raise_()
        self.tabWidget.raise_()
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
        self.file_menu.addAction(self.actionSet_Root_Directory)
        self.file_menu.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSet_Root_Directory.setText(QCoreApplication.translate("MainWindow", u"Set Root Directory", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scriptBrowser_tab), QCoreApplication.translate("MainWindow", u"Script Browser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.showBuilder_tab), QCoreApplication.translate("MainWindow", u"Show Builder", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shotBuilder_tab), QCoreApplication.translate("MainWindow", u"Shot Builder", None))
#if QT_CONFIG(accessibility)
        self.scriptBrowser_widget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.rootDir_lineEdit.setInputMask("")
        self.rootDir_lineEdit.setText("")
        self.rootDir_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Root Directory", None))
        self.updateScriptsList_pushButton.setText(QCoreApplication.translate("MainWindow", u"Update Scripts List", None))
        self.launchNukeIndie_pushButton.setText(QCoreApplication.translate("MainWindow", u"Launch Nuke Indie", None))
        self.Directory_label.setText(QCoreApplication.translate("MainWindow", u"Directory:", None))
        self.show_label.setText(QCoreApplication.translate("MainWindow", u"Show:", None))
        self.shot_label.setText(QCoreApplication.translate("MainWindow", u"Shot: ", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

