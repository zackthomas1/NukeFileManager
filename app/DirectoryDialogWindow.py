import sys 
import logging

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Gui
from __QtFiles__.DirectoryDialog_v001 import Ui_Directory_Dialog

# 
from modules.Utilities import Utilities

# Data Models
from modules.dataModels.ScriptsListModel import ScriptsListModel
from modules.dataModels.ShotCodeModel import ShotCodeModel
from modules.dataModels.ShowCodeModel import ShowCodeModel

class DirectoryDialog(QDialog, Ui_Directory_Dialog): 
    def __init__(self, MainWindowInstance, ScriptsBrowserInstance):
        logging.debug("DirectoryDialog::__init__-> initalizing MainWindow class")
        super().__init__()
        self.setupUi(self)

        # 
        self.scriptsBrowserInstance = ScriptsBrowserInstance
        self.mainWindowInstance = MainWindowInstance

        # Load json files 
        # ----------------
        # load saved root directory
        rootDirSaveFile = "C:\\Dev\\Python\\PracticeProjects\\NukeFileManager\\json\\rootDirSave.json" # Remove absolute path
        try:
            self.mainWindowInstance.rootDirModel.directory = Utilities.load_json(rootDirSaveFile)
            self.directory_lineEdit.setText(self.mainWindowInstance.rootDirModel.directory)
            self.entered_root_dir()
        except Exception: 
            logging.error("ERROR << DirectoryDialog::__init__-> Utilites.load_json call failed")


        # Slot-Signal connections 
        # -----------------------
        self.ok_buttonBox.accepted.connect(self.entered_root_dir)
        self.ok_buttonBox.rejected.connect(self.close_directory_dialog_window)

    def entered_root_dir(self): 
        """ """ 
        try:
            self.scriptsBrowserInstance.set_root_dir(self.directory_lineEdit.text())

            # Update show_comboBox
            self.mainWindowInstance.showCode_comboBox.setCurrentIndex(-1)
            self.scriptsBrowserInstance.update_shows_list(self.mainWindowInstance.showCodeModel)
            self.mainWindowInstance.showCodeModel.layoutChanged.emit()
            logging.debug("DirectoryDialogWindow::entered_root_dir-> " +
                    "Updating showCode_comboBox with: %s" % self.mainWindowInstance.showCodeModel.shows)
           
            if self.mainWindowInstance.shotCodeModel.shots != []: 
                # Update show_comboBox
                self.mainWindowInstance.shotCode_comboBox.setCurrentIndex(-1)
                self.mainWindowInstance.shotCodeModel.shots = []
                # self.scriptsBrowserInstance.update_shots_list(self.mainWindowInstance.showCodeModel)
                self.mainWindowInstance.shotCodeModel.layoutChanged.emit()
                logging.debug("DirectoryDialogWindow::entered_root_dir-> " +
                        "Emptying shotCode_comboBox.")
            self.hide() 

        except Exception:

            self.mainWindowInstance.showCode_comboBox.setCurrentIndex(-1)
            self.mainWindowInstance.showCodeModel.shows= []
            self.mainWindowInstance.showCodeModel.layoutChanged.emit()

            self.mainWindowInstance.shotCode_comboBox.setCurrentIndex(-1)
            self.mainWindowInstance.shotCodeModel.shots = []
            self.mainWindowInstance.shotCodeModel.layoutChanged.emit()

            logging.error("ERROR << DirectoryDialogWindow::entered_root_dir-> " + 
                    "could not obtain valid root director from ScriptsBrowser.set_root_dir()")
        
        # Clear scripts_listView if root directory is updated 
        if self.mainWindowInstance.scriptsViewModel.scripts != []: 
            self.mainWindowInstance.scriptsViewModel.scripts = [] 
            self.mainWindowInstance.scriptsViewModel.layoutChanged.emit()

    def close_directory_dialog_window(self): 
        """ """ 

        logging.debug("DirectoryDialogWindow::close_directory_dialog_window-> hiding directory dialog ")
        self.hide()