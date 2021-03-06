import sys
import logging

from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

from __QtFiles__.NukeFileMangerGUI_v001 import Ui_MainWindow
from modules.FileManger import FileManger

class MainWindow(QMainWindow, Ui_MainWindow): 

    fileMan = FileManger()

    def __init__(self): 
        super().__init__()

        self.setupUi(self)
        self.show()

        self.rootDir_lineEdit.returnPressed.connect(self.enter_root_dir)
        self.showCode_lineEdit.returnPressed.connect(self.enter_show_code)
        self.shotCode_lineEdit.returnPressed.connect(self.enter_shot_code)

        self.enter_shotinfo_pushButton.pressed.connect(self.pressed_enter_shotinfo)

        self.launchNukeIndie_pushButton.pressed.connect(self.pressed_launch_nukeindie)



    def pressed_launch_nukeindie(self): 
        logging.debug("MainWindow::launch_nukeindie-> from FileManger calling static launch_nukeindie method")
        FileManger.launch_nukeindie()

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

    def enter_shot_code(self):
        inputShotCode = self.shotCode_lineEdit.text()
        logging.debug("MainWindow::enter_shot_code -> " + 
                        "from FileManger calling set_shot_code method " + 
                        "with parameter: " + inputShotCode)
        self.fileMan.set_shot_code(inputShotCode)

    def pressed_enter_shotinfo(self): 
        logging.debug("MainWindow::pressed_enter_shotinfo -> " + 
                        "from FileManger calling ____ method ")

    


