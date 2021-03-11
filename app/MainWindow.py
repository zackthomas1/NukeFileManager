import sys
import logging

from PySide2.QtCore import *
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

from __QtFiles__.NukeFileMangerGUI_v004 import Ui_MainWindow

from modules.ScriptsBrowser import ScriptsBrowser
from modules.Utilities import Utilities

from modules.dataModels.ScriptsListModel import ScriptsListModel
from modules.dataModels.ShotCodeModel import ShotCodeModel
from modules.dataModels.ShowCodeModel import ShowCodeModel

class MainWindow(QMainWindow, Ui_MainWindow): 

    scriptsBrowser = ScriptsBrowser()

    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.show()

        # Set up scripts list view model 
        # ------------------------------
        # Script list view    
        self.scriptsViewModel = ScriptsListModel()
        self.scripts_listView.setModel(self.scriptsViewModel)

        # Show comboBox
        self.showCodeModel = ShowCodeModel() 
        self.showCode_comboBox.setModel(self.showCodeModel)

        # Shot comboBox
        self.shotCodeModel = ShotCodeModel()
        self.shotCode_comboBox.setModel(self.shotCodeModel)

        # Load json files 
        # ----------------
        # load saved root directory
        rootDirSaveFile = "C:\\Dev\\Python\\PracticeProjects\\NukeFileManager\\json\\rootDirSave.json" # Remove absolute path
        if Utilities.load_json(rootDirSaveFile) != None:
            self.rootDir_lineEdit.setText(Utilities.load_json(rootDirSaveFile))
            self.entered_root_dir()

        # UI_MainWindow Style adjustments
        # -------------------------------
        
        # Slot-Signal connections 
        # -----------------------
        self.scripts_listView.doubleClicked.connect(self.calling_launch_nukeindie)

        self.rootDir_lineEdit.editingFinished.connect(self.entered_root_dir)
        self.showCode_comboBox.currentIndexChanged.connect(self.selected_show_code)
        self.shotCode_comboBox.currentIndexChanged.connect(self.selected_shot_code)

        self.enter_shotinfo_pushButton.pressed.connect(self.calling_update_scriptsList)

        self.launchNukeIndie_pushButton.pressed.connect(self.calling_launch_nukeindie)

    def entered_root_dir(self): 
        inputRootDir = self.rootDir_lineEdit.text()
        logging.debug("MainWindow::entered_root_dir -> " + 
                        "ScriptsBrowser.set_root_dir() method " + 
                        "with parameter: %s" % inputRootDir)

        self.scriptsBrowser.set_root_dir(inputRootDir)
        
        # Clear scripts_listView 
        if self.scriptsViewModel.scripts != []: 
            self.scriptsViewModel.scripts = [] 
            self.scriptsViewModel.layoutChanged.emit()

        # Updating show comboBox
        self.showCode_comboBox.setCurrentIndex(-1)
        showList = self.scriptsBrowser.get_shows_list()
        self.showCodeModel.shows = showList
        self.showCodeModel.layoutChanged.emit()
        logging.debug("MainWindow::entered_root_dir-> Updating showCode_comboBox with: %s" % showList)

    def selected_show_code(self):

        # Retrieve string of selected comboBox index
        index = self.showCode_comboBox.currentIndex() 
        inputShowCode = self.showCode_comboBox.itemText(index)

        logging.debug("MainWindow::selected_show_code -> " + 
                        "calling ScriptsBrowser.set_show_code() method " + 
                        "with parameter: %s" % inputShowCode)

        self.scriptsBrowser.set_show_code(inputShowCode)

        # Updating shot comboBox
        self.shotCode_comboBox.setCurrentIndex(-1)
        shotList = self.scriptsBrowser.get_shots_list()
        self.shotCodeModel.shots = shotList
        self.shotCodeModel.layoutChanged.emit()
        logging.debug("MainWindow::selected_show_code-> Updating shotCode_comboBox with: %s" % shotList)

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
            self.scriptsViewModel.scripts = self.scriptsBrowser.update_scriptsList()
            self.scriptsViewModel.layoutChanged.emit()
            logging.debug("MainWindow::calling_update_shotList-> scriptsViewModel Updated")
        except Exception: 
            self.scriptsViewModel.scripts = []
            self.scriptsViewModel.layoutChanged.emit()
            logging.error("Error << MainWindow::calling_update_shotList-> "+
                        "Unable to retrieve valid scripts list from ScriptsBrowser.update_shotList()")

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
