# 
import sys
import logging

# pyside2 
from PySide2.QtCore import *
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

# GUI from Qt Designer
from __QtFiles__.NukeFileMangerGUI_v004 import Ui_MainWindow

#
from app.DirectoryDialogWindow import DirectoryDialog

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

        # Set up dialog windows
        # -------------------------
        self.directoryDialog = DirectoryDialog() 
      
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

        # Load json files 
        # ----------------
        # load saved root directory
        rootDirSaveFile = "C:\\Dev\\Python\\PracticeProjects\\NukeFileManager\\json\\rootDirSave.json" # Remove absolute path
        self.rootDirModel.directory = Utilities.load_json(rootDirSaveFile)
        if self.rootDirModel.directory != None:
            self.rootDir_lineEdit.setText(self.rootDirModel.directory)
            self.entered_root_dir()

        # UI_MainWindow Style adjustments
        # -------------------------------
        
        # Slot-Signal connections 
        # -----------------------
        # Menu
        self.actionSet_Root_Directory.triggered.connect(self.open_root_dir_dialog) 

        # Scripts browser
        self.scripts_listView.doubleClicked.connect(self.calling_launch_nukeindie)

        self.rootDir_lineEdit.editingFinished.connect(self.entered_root_dir)
        self.showCode_comboBox.currentIndexChanged.connect(self.selected_show_code)
        self.shotCode_comboBox.currentIndexChanged.connect(self.selected_shot_code)

        self.updateScriptsList_pushButton.pressed.connect(self.calling_update_scriptsList)

        self.launchNukeIndie_pushButton.pressed.connect(self.calling_launch_nukeindie)

    def open_root_dir_dialog(self): 
        """Show/hide root directory dialog window""" 
        logging.debug("MainWindow::open_root_dir_dialog->calling DirectoryDialog class")

        if self.directoryDialog.isVisible():
            self.directoryDialog.hide()
        else: 
            self.directoryDialog.show()
        
    def entered_root_dir(self): 
        self.rootDirModel.directory = self.rootDir_lineEdit.text()
        logging.debug("MainWindow::entered_root_dir-> " + 
                    "ScriptsBrowser.set_root_dir() method " + 
                    "with parameter: %s" % self.rootDirModel.directory)

        try:
            self.scriptsBrowser.set_root_dir(self.rootDirModel.directory)

            # Update show_comboBox
            self.showCode_comboBox.setCurrentIndex(-1)
            self.scriptsBrowser.update_shows_list(self.showCodeModel)
            self.showCodeModel.layoutChanged.emit()
            logging.debug("MainWindow::entered_root_dir-> " +
                    "Updating showCode_comboBox with: %s" % self.showCodeModel.shows)

        except Exception: 
            self.rootDir_lineEdit.setText("")
            self.showCode_comboBox.setCurrentIndex(-1)
            self.showCodeModel.shows= []
            self.showCodeModel.layoutChanged.emit()
            self.shotCode_comboBox.setCurrentIndex(-1)
            self.shotCodeModel.shots = []
            self.shotCodeModel.layoutChanged.emit()
            logging.error("ERROR << MainWindow::entered_root_dir-> " + 
                    "could not obtain valid root director from ScriptsBrowser.set_root_dir()")

        # Clear scripts_listView if root directory is updated 
        if self.scriptsViewModel.scripts != []: 
            self.scriptsViewModel.scripts = [] 
            self.scriptsViewModel.layoutChanged.emit()

    def selected_show_code(self):

        # Retrieve string of selected comboBox index
        index = self.showCode_comboBox.currentIndex() 
        inputShowCode = self.showCode_comboBox.itemText(index)

        logging.debug("MainWindow::selected_show_code -> " + 
                "calling ScriptsBrowser.set_show_code() method " + 
                "with parameter: %s" % inputShowCode)

        self.scriptsBrowser.set_show_code(inputShowCode)

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

    def calling_update_scriptsList(self): 
        logging.debug("MainWindow::calling_update_shotList -> " + 
                        "calling ScriptsBrowser.update_shotList() method ")

        try:
            self.scriptsBrowser.update_scripts_list(self.scriptsViewModel)
            self.scriptsViewModel.layoutChanged.emit()
            logging.debug("MainWindow::calling_update_shotList-> scriptsViewModel Updated")
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
