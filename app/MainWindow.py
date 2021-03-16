# 
import sys
import logging

# pyside2 
from PySide2.QtCore import *
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

# GUI from Qt Designer
from __QtFiles__.MainWindow.NukeFileMangerGUI_v005 import Ui_MainWindow

#
from app.SettingsDialog import SettingsDialog

#
from modules.ScriptsBrowser import ScriptsBrowser
from modules.Utilities import Utilities

# Data Models
from modules.dataModels.RootDirectoryModel import RootDirectoryModel
from modules.dataModels.ScriptsListModel import ScriptsListModel
from modules.dataModels.ShotCodeModel import ShotCodeModel
from modules.dataModels.ShowCodeModel import ShowCodeModel

class MainWindow(QMainWindow, Ui_MainWindow): 
    scriptsBrowser = ScriptsBrowser()

    def __init__(self): 
        logging.debug("MainWindow::__init__-> initalizing MainWindow class")
        super().__init__()
        self.setupUi(self)
        self.show()
      
        # Set up scripts list view model 
        # ------------------------------
        # Root Directory Model
        self.rootDirModel = RootDirectoryModel()

        # Show comboBox
        self.showCodeModel = ShowCodeModel() 
        self.showCode_comboBox.setModel(self.showCodeModel)

        # Shot comboBox
        self.shotCodeModel = ShotCodeModel()
        self.shotCode_comboBox.setModel(self.shotCodeModel)

        # Script list view    
        self.scriptsViewModel = ScriptsListModel()
        self.scripts_listView.setModel(self.scriptsViewModel)

        # Set up dialog windows
        # -------------------------
        self.settingsDialog = SettingsDialog(self, self.scriptsBrowser) 

        # UI_MainWindow Style adjustments
        # -------------------------------
        
        # Slot-Signal connections 
        # -----------------------
        # Menu
        self.openSettings_action.triggered.connect(self.open_root_dir_dialog) 

        # Scripts browser
        self.scripts_listView.doubleClicked.connect(self.calling_launch_nukeindie)

        self.showCode_comboBox.currentIndexChanged.connect(self.selected_show_code)
        self.shotCode_comboBox.currentIndexChanged.connect(self.selected_shot_code)

        self.updateScriptsList_pushButton.pressed.connect(self.calling_update_scripts_list)

        self.launchNukeIndie_pushButton.pressed.connect(self.calling_launch_nukeindie)

    def open_root_dir_dialog(self): 
        """Show/hide root directory dialog window""" 
        logging.debug("MainWindow::open_root_dir_dialog-> calling DirectoryDialog class")

        if self.settingsDialog.isVisible():
            self.settingsDialog.hide()
        else: 
            self.settingsDialog.show()
        
    def selected_show_code(self):

        # Retrieve string of selected comboBox index
        index = self.showCode_comboBox.currentIndex() 
        inputShowCode = self.showCode_comboBox.itemText(index)

        logging.debug("MainWindow::selected_show_code -> " + 
                "calling ScriptsBrowser.set_show_code() method " + 
                "with parameter: %s" % inputShowCode)

        self.scriptsBrowser.set_show_code(inputShowCode)
        if index != -1:
            # Updating shot comboBox
            try:
                self.shotCode_comboBox.setCurrentIndex(-1)
                self.scriptsBrowser.update_shots_list(self.shotCodeModel)
                self.shotCodeModel.layoutChanged.emit()
                logging.debug("MainWindow::selected_show_code-> " + 
                        "Updating shotCode_comboBox with: %s" % inputShowCode)
            except Exception:
                self.shotCodeModel.shots = []
                self.shotCodeModel.layoutChanged.emit()
                logging.error("ERROR << MainWindow::calling_update_shot_list-> "+
                        "Unable to retrieve valid shots list from ScriptsBrowser.update_shot_list()")

    def selected_shot_code(self): 

        # Retrieve string of selected comboBox index
        index = self.shotCode_comboBox.currentIndex()
        inputShotCode = self.shotCode_comboBox.itemText(index)

        logging.debug("MainWindow::selected_shot_code-> " + 
                        "calling ScriptsBrowser.set_shot_code() method " +
                        "with parameter: %s" % str(inputShotCode))
        self.scriptsBrowser.set_shot_code(inputShotCode)

    def calling_update_scripts_list(self): 
        logging.debug("MainWindow::calling_update_scripts_list -> " + 
                        "calling ScriptsBrowser.update_scripts_list() method ")

        try:
            self.scriptsBrowser.update_scripts_list(self.scriptsViewModel)
            self.scriptsViewModel.layoutChanged.emit()
            logging.debug("MainWindow::calling_update_scripts_list-> scriptsViewModel Updated")
        except Exception: 
            self.scriptsViewModel.scripts = []
            self.scriptsViewModel.layoutChanged.emit()
            logging.error("ERROR << MainWindow::calling_update_scripts_list-> "+
                        "Unable to retrieve valid scripts list from ScriptsBrowser.update_scripts_list()")

    def calling_launch_nukeindie(self): 
        
        # Gets Indexes (list of a single item, since nkFiles_listView is in single select mode)
        indexes = self.scripts_listView.selectedIndexes() 

        # If script is selected
        if indexes: 
            index = indexes[0]
            scriptName = self.scriptsViewModel.scripts[index.row()]
            logging.debug("MainWindow::calling_launch_nukeindie-> " +
                            "calling ScriptsBrowser.launch_nukeindie() method" + 
                            "with parameter %s" % scriptName)
            self.scriptsBrowser.launch_nukeindie(scriptName)
        else:
            logging.debug("MainWindow::calling_launch_nukeindie-> " +
                            "calling ScriptsBrowser.launch_nukeindie() method")
            self.scriptsBrowser.launch_nukeindie()
