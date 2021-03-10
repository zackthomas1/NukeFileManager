import sys
import logging

from PySide2.QtCore import *
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

from __QtFiles__.NukeFileMangerGUI_v002 import Ui_MainWindow
from modules.FileManger import FileManger
from modules.ScriptsListModel import ScriptsListModel
from modules.ShotCodeModel import ShotCodeModel
from modules.ShowCodeModel import ShowCodeModel

class MainWindow(QMainWindow, Ui_MainWindow): 

    fileMan = FileManger()

    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.show()

        # Set up scripts list view model 
        # ------------------------------
        # Script list view    
        self.scriptsViewModel = ScriptsListModel()
        self.nkFiles_listView.setModel(self.scriptsViewModel)

        # Show comboBox
        self.showCodeModel = ShowCodeModel() 
        self.showCode_comboBox.setModel(self.showCodeModel)

        # Shot comboBox
        self.shotCodeModel = ShotCodeModel()
        self.shotCode_comboBox.setModel(self.shotCodeModel)

        # UI_MainWindow Style adjustments
        # -------------------------------
        
        # Slot-Signal connections 
        # -----------------------

        self.nkFiles_listView.doubleClicked.connect(self.doubleClick_script)

        self.rootDir_lineEdit.editingFinished.connect(self.entered_root_dir)
        self.showCode_comboBox.currentIndexChanged.connect(self.selected_show_code)
        self.shotCode_comboBox.currentIndexChanged.connect(self.selected_shot_code)

        self.enter_shotinfo_pushButton.pressed.connect(self.pressed_update_shotList)

        self.launchNukeIndie_pushButton.pressed.connect(self.pressed_launch_nukeindie)

    def doubleClick_script(self): 

        # Gets Indexes (list of a single item, since nkFiles_listView is in single select mode)
        indexes = self.nkFiles_listView.selectedIndexes()

        if indexes: 
            # Indexes is a list of a single item in single-select mode
            index = indexes[0]
            scriptName = self.scriptsViewModel.scripts[index.row()]
            logging.debug("MainWindow::doubleClick_script-> " +
                        "from FileManger calling doubleClick_launch_script_nukeIndie() method " +
                        "with parameter: " + scriptName)
            self.fileMan.doubleClick_launch_script_nukeIndie(scriptName)
        else: 
            logging.error("ERROR: MainWindow::doubleClick_script-> no index selected")
            raise Exception

    def entered_root_dir(self): 
        inputRootDir = self.rootDir_lineEdit.text()
        logging.debug("MainWindow::enter_root_dir -> " + 
                        "from FileManger calling set_path_baseName method " + 
                        "with parameter: " + inputRootDir)

        self.fileMan.set_root_dir(inputRootDir)

        # Updating show comboBox
        self.showCode_comboBox.setCurrentIndex(-1)
        showList = self.fileMan.get_shows_list()
        self.showCodeModel.shows = showList
        self.showCodeModel.layoutChanged.emit()
        logging.debug("MainWindow::enter_root_dir-> Updating showCode_comboBox with: %s" % showList)


    def selected_show_code(self):

        # Retrieve string of selected comboBox index
        index = self.showCode_comboBox.currentIndex() 
        inputShowCode = self.showCode_comboBox.itemText(index)

        logging.debug("MainWindow::enter_show_code -> " + 
                        "from FileManger calling set_show_code method " + 
                        "with parameter: " + inputShowCode)

        self.fileMan.set_show_code(inputShowCode)

        # Updating shot comboBox
        self.shotCode_comboBox.setCurrentIndex(-1)
        shotList = self.fileMan.get_shots_list()
        self.shotCodeModel.shots = shotList
        self.shotCodeModel.layoutChanged.emit()
        logging.debug("MainWindow::enter_show_code-> Updating shotCode_comboBox with: %s" % shotList)

    def selected_shot_code(self): 

        # Retrieve string of selected comboBox index
        index = self.shotCode_comboBox.currentIndex()
        inputShotCode = self.shotCode_comboBox.itemText(index)

        logging.debug("MainWindow::enter_shot_code -> " + 
                        "from FileManger calling set_shot_code method " +
                        "with parameter: %s" % str(inputShotCode))
        self.fileMan.set_shot_code(inputShotCode)

    def pressed_update_shotList(self): 
        logging.debug("MainWindow::pressed_update_shotList -> " + 
                        "from FileManger calling update_shotList() method ")

        self.scriptsViewModel.scripts = self.fileMan.update_shotList()
        self.scriptsViewModel.layoutChanged.emit()
        logging.debug("MainWindow::pressed_update_shotList-> scriptsViewModel Updated")

    def pressed_launch_nukeindie(self): 
        
        indexes = self.nkFiles_listView.selectedIndexes() 

        # If script is selected
        if indexes: 
            index = indexes[0]
            scriptName = self.scriptsViewModel.scripts[index.row()]
            self.fileMan.launch_nukeindie(scriptName)
            logging.debug("MainWindow::launch_nukeindie-> " +
                            "from FileManger calling launch_nukeindie method" + 
                            "with parameter")
        else:
            self.fileMan.launch_nukeindie()
            logging.debug("MainWindow::launch_nukeindie-> " +
                            "from FileManger calling launch_nukeindie method")