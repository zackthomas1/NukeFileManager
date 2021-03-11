import sys 
import logging

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from __QtFiles__.DirectoryDialog_v001 import Ui_Directory_Dialog

# Data Models
from modules.dataModels.ScriptsListModel import ScriptsListModel
from modules.dataModels.ShotCodeModel import ShotCodeModel
from modules.dataModels.ShowCodeModel import ShowCodeModel

class DirectoryDialog(QDialog, Ui_Directory_Dialog): 
    def __init__(self):
        logging.debug("DirectoryDialog::__init__-> initalizing MainWindow class")
        super().__init__()
        self.setupUi(self)
        #self.show()

        self.ok_buttonBox.accepted.connect(self.clicked_ok)
        self.ok_buttonBox.rejected.connect(self.clicked_cancel)

    def clicked_ok(self): 
        """ """ 
        inputRootDir = self.directory_lineEdit.text()

        logging.debug("DirectoryDialogWindow::clicked_ok-> ")

    def clicked_cancel(self): 
        """ """ 

        logging.debug("DirectoryDialogWindow::clicked_cancel-> hiding directory dialog ")
        self.hide()