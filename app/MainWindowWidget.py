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

        # Set up data models
        # ------------------------------
        # Root Directory Model
        self.rootDirModel = RootDirectoryModel()

        # Show Model
        self.showCodeModel = ShowCodeModel() 

        # Shot Model 
        self.shotCodeModel = ShotCodeModel()

        # Script listWiew Model   
        self.scriptsViewModel = ScriptsListModel()

        # UI_MainWindow Style adjustments
        # -------------------------------
        # Tabs
        self.tabWidget.clear()

        # script browser
        self.scriptBrowserTab_Widget = ScriptBrowserWidget(self.rootDirModel, self.showCodeModel, 
                                                            self.shotCodeModel,  self.scriptsViewModel)
        self.scriptBrowserTab_Widget.setObjectName(u"scriptBrowser_tab")
        self.tabWidget.addTab(self.scriptBrowserTab_Widget, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scriptBrowserTab_Widget), 
                                    QCoreApplication.translate("MainWindow", u"Script Browser", None))
        
        # shot builder
        self.shotBuilderTab_Widget = ShotBuilderWidget(self.rootDirModel, self.showCodeModel, 
                                                        self.shotCodeModel )
        self.shotBuilderTab_Widget.setObjectName(u"shotBuilder_tab")
        self.tabWidget.addTab(self.shotBuilderTab_Widget, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shotBuilderTab_Widget), 
                                    QCoreApplication.translate("MainWindow", u"Shot Builder", None))

        # show builder
        self.showBuilderTab_Widget = ShowBuilderWidget(self.rootDirModel, self.showCodeModel)
        self.showBuilderTab_Widget.setObjectName(u"showBuilder_tab")
        self.tabWidget.addTab(self.showBuilderTab_Widget, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.showBuilderTab_Widget), 
                                    QCoreApplication.translate("MainWindow", u"Show Builder", None))

        # Slot-Signal connections 
        # -----------------------
        # Menu
        self.openSettings_action.triggered.connect(self.open_settings_dialog) 

        # Set up dialog windows
        # -------------------------
        self.settingsDialog = SettingsDialog(self.scriptBrowserTab_Widget, self.scriptBrowserTab_Widget.scriptsBrowser) 
        self.setCentralWidget(self.tabWidget)
 
    def open_settings_dialog(self): 
        """Show/hide root directory dialog window""" 
        
        logging.debug("MainWindow::open_settings_dialog-> calling SettingsDialog class")

        if self.settingsDialog.isVisible():
            self.settingsDialog.hide()
        else: 
            self.settingsDialog.show()
        