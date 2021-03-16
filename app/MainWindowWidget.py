import sys
import logging

# pyside2 
from PySide2.QtCore import *
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

# GUI from Qt Designer
from __QtFiles__.MainWindow.NukeFileMangerGUI_v006 import Ui_MainWindow

# Custom Widgets
from app.ScriptsBrowserWidget import ScriptBrowserWidget
from app.ShotBuilderWidget import ShotBuilderWidget
from app.ShowBuilderWidget import ShowBuilderWidget
from app.SettingsDialogWidget import SettingsDialog

# modules
from modules.ScriptsBrowser import ScriptsBrowser
from modules.Utilities import Utilities

# Data Models
from modules.dataModels.RootDirectoryModel import RootDirectoryModel
from modules.dataModels.ScriptsListModel import ScriptsListModel
from modules.dataModels.ShotCodeModel import ShotCodeModel
from modules.dataModels.ShowCodeModel import ShowCodeModel


class MainWindowWidget(QMainWindow, Ui_MainWindow): 
    scriptsBrowser = ScriptsBrowser()

    def __init__(self): 
        logging.debug("MainWindow::__init__-> initalizing MainWindow class")
        super().__init__()
        self.setupUi(self)
        self.show()

        # Slot-Signal connections 
        # -----------------------
        # Menu
        self.openSettings_action.triggered.connect(self.open_settings_dialog) 

        # UI_MainWindow Style adjustments
        # -------------------------------
        # Tabs
        self.tabWidget.clear()
        self.scriptBrowserTab_Widget = ScriptBrowserWidget()
        self.scriptBrowserTab_Widget.setObjectName(u"scriptBrowser_tab")
        self.tabWidget.addTab(self.scriptBrowserTab_Widget, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scriptBrowserTab_Widget), QCoreApplication.translate("MainWindow", u"Script Browser", None))
        
        self.shotBuilderTab_Widget = ShotBuilderWidget()
        self.shotBuilderTab_Widget.setObjectName(u"shotBuilder_tab")
        self.tabWidget.addTab(self.shotBuilderTab_Widget, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shotBuilderTab_Widget), QCoreApplication.translate("MainWindow", u"Shot Builder", None))

        self.showBuilderTab_Widget = ShowBuilderWidget()
        self.showBuilderTab_Widget.setObjectName(u"showBuilder_tab")
        self.tabWidget.addTab(self.showBuilderTab_Widget, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.showBuilderTab_Widget), QCoreApplication.translate("MainWindow", u"Show Builder", None))

        # Set up dialog windows
        # -------------------------
        self.settingsDialog = SettingsDialog(self.scriptBrowserTab_Widget, self.scriptBrowserTab_Widget.scriptsBrowser) 

        self.setCentralWidget(self.tabWidget)
 

    def open_settings_dialog(self): 
        """Show/hide root directory dialog window""" 
        logging.debug("MainWindow::open_settings_dialog-> calling DirectoryDialog class")

        if self.settingsDialog.isVisible():
            self.settingsDialog.hide()
        else: 
            self.settingsDialog.show()
        