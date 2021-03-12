import sys, logging

from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

class RootDirectoryModel(): 
    def __init__(self, directory = None):
        super().__init__()
        self.directory = directory or ""
        logging.debug("RootDirectoryModel::__init__-> Initiating root directory model")

    def data(self, index, role): 
        if role == Qt.DisplayRole: 

            directoryName = self.scripts[index.row()]
            return directoryName 

    def rowCount(self, index): 
        return len(self.directory)


