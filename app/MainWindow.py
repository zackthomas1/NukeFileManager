import sys
import logging

from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

from __QtFiles__.NukeFileMangerGUI_v002 import Ui_MainWindow
from modules.FileManger import FileManger
from modules.ScriptsListViewModel import ScriptsListViewModel

class MainWindow(QMainWindow, Ui_MainWindow): 

    fileMan = FileManger()

    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.show()

        # Set up scripts list view model 
        # ------------------------------
        self.scriptsViewModel = ScriptsListViewModel()
        self.nkFiles_listView.setModel(self.scriptsViewModel)

        # UI_MainWindow Style adjustments
        # -------------------------------
        self.shotCode_comboBox.setPlaceholderText("Shot Code")

        # Slot-Signal connections 
        # -----------------------

        self.nkFiles_listView.doubleClicked.connect(self.doubleClick_script)

        self.rootDir_lineEdit.editingFinished.connect(self.enter_root_dir)
        self.showCode_lineEdit.editingFinished.connect(self.enter_show_code)
        self.shotCode_lineEdit.editingFinished.connect(self.enter_shot_code)

        self.enter_shotinfo_pushButton.pressed.connect(self.pressed_enter_shotinfo)

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

    def enter_root_dir(self): 
        inputRootDir = self.rootDir_lineEdit.text()
        logging.debug("MainWindow::enter_root_dir -> " + 
                        "from FileManger calling set_path_baseName method " + 
                        "with parameter: " + inputRootDir)
        self.fileMan.set_root_dir(inputRootDir)

    def enter_show_code(self): 
        inputShowCode = self.showCode_lineEdit.text()
        logging.debug("MainWindow::enter_show_code -> " + 
                        "from FileManger calling set_show_code method " + 
                        "with parameter: " + inputShowCode)

        self.fileMan.set_show_code(inputShowCode)

        shotList = self.fileMan.get_shots_list()
        logging.debug("MainWindow::enter_show_code-> Updating shotCode_comboBox with: %s" % shotList)
        self.shotCode_comboBox.clear()
        self.shotCode_comboBox.addItems(shotList)

    def enter_shot_code(self):
        inputShotCode = self.shotCode_lineEdit.text()
        logging.debug("MainWindow::enter_shot_code -> " + 
                        "from FileManger calling set_shot_code method " + 
                        "with parameter: " + inputShotCode)
        self.fileMan.set_shot_code(inputShotCode)

    def pressed_enter_shotinfo(self): 
        logging.debug("MainWindow::pressed_enter_shotinfo -> " + 
                        "from FileManger calling enter_shotinfo() method ")


        self.scriptsViewModel.scripts = self.fileMan.enter_shotinfo()
        self.scriptsViewModel.layoutChanged.emit()
        logging.debug("MainWindow::pressed_enter_shotinfo-> scriptsViewModel Updated")

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