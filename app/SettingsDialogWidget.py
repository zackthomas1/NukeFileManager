import sys 
import logging

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# GUI from Qt Designer
from __QtFiles__.Dialogs.SettingDialog_v001 import Ui_Settings_Dialog

# Modules
from modules.Utilities import Utilities

# Data Models
from modules.dataModels.ScriptsListModel import ScriptsListModel
from modules.dataModels.ShotCodeModel import ShotCodeModel
from modules.dataModels.ShowCodeModel import ShowCodeModel

class SettingsDialog(QDialog, Ui_Settings_Dialog): 
    def __init__(self, WidgetInstance, ScriptsBrowserInstance):
        logging.debug("SettingsDialog::__init__-> initalizing MainWindow class")
        super().__init__()
        self.setupUi(self)

        # 
        self.scriptsBrowserInstance = ScriptsBrowserInstance
        self.widgetInstance = WidgetInstance

        # Load json files 
        # ----------------
        # load saved root directory
        try:
            rootDirSaveFile = self.scriptsBrowserInstance.rootDirSaveFile
            self.widgetInstance.rootDirModel.directory = Utilities.load_json(rootDirSaveFile)
            self.rootDirectory_lineEdit.setText(self.widgetInstance.rootDirModel.directory)
            self.entered_root_dir()
        except Exception: 
            logging.error("ERROR << SettingsDialog::__init__-> Utilites.load_json call failed")


        # 
        self.NukeExe_lineEdit.setText(self.scriptsBrowserInstance.exePath)

        # Slot-Signal connections 
        # -----------------------  
        # self.NukeExe_lineEdit.selectionChanged.connect()
        self.ok_buttonBox.accepted.connect(self.enter_confirm_settings)
        self.ok_buttonBox.rejected.connect(self.close_directory_dialog_window)

    def entered_root_dir(self): 
        """ """ 
        try:
            self.scriptsBrowserInstance.set_root_dir(self.rootDirectory_lineEdit.text())

            # Update show_comboBox
            self.widgetInstance.showCode_comboBox.setCurrentIndex(-1)
            self.scriptsBrowserInstance.update_shows_list(self.widgetInstance.showCodeModel)
            self.widgetInstance.showCodeModel.layoutChanged.emit()
            logging.debug("SettingsDialog::entered_root_dir-> " +
                    "Updating showCode_comboBox with: %s" % self.widgetInstance.showCodeModel.shows)
           
            if self.widgetInstance.shotCodeModel.shots != []: 
                # Update show_comboBox
                self.widgetInstance.shotCode_comboBox.setCurrentIndex(-1)
                self.widgetInstance.shotCodeModel.shots = []
                # self.scriptsBrowserInstance.update_shots_list(self.widgetInstance.showCodeModel)
                self.widgetInstance.shotCodeModel.layoutChanged.emit()
                logging.debug("SettingsDialog::entered_root_dir-> " +
                        "Emptying shotCode_comboBox.")

        except Exception:

            self.widgetInstance.showCode_comboBox.setCurrentIndex(-1)
            self.widgetInstance.showCodeModel.shows= []
            self.widgetInstance.showCodeModel.layoutChanged.emit()

            self.widgetInstance.shotCode_comboBox.setCurrentIndex(-1)
            self.widgetInstance.shotCodeModel.shots = []
            self.widgetInstance.shotCodeModel.layoutChanged.emit()

            logging.error("ERROR << SettingsDialog::entered_root_dir-> " + 
                    "could not obtain valid root director from ScriptsBrowser.set_root_dir()")
        
        # Clear scripts_listView if root directory is updated 
        if self.widgetInstance.scriptsViewModel.scripts != []: 
            self.widgetInstance.scriptsViewModel.scripts = [] 
            self.widgetInstance.scriptsViewModel.layoutChanged.emit()

    def enter_nuke_exe_path(self): 
        """ """
        logging.debug("SettingsDialog::enter_nuke_exe_path-> " + 
                    "calling ScriptsBrowser.set_nuke_exe_path" + 
                    "with parameter '%s'" % self.NukeExe_lineEdit.text())
        self.scriptsBrowserInstance.set_nuke_exe_path(self.NukeExe_lineEdit.text())


    def enter_confirm_settings(self):

        self.entered_root_dir() 
        self.enter_nuke_exe_path()

        self.hide()

    def close_directory_dialog_window(self): 
        """ """ 

        logging.debug("DirectoryDialogWindow::close_directory_dialog_window-> hiding directory dialog ")
        self.hide()