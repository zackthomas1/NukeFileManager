import sys, logging

from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

class ScriptsListModel(QAbstractListModel): 
    def __init__(self, scripts = None):
        super().__init__()
        self.scripts = scripts or [] 
        logging.debug("ScriptsListModel::__init__-> Initiating scripts listView Model")

    def data(self, index, role): 
        if role == Qt.DisplayRole: 
            
            scriptName = self.scripts[index.row()]
            return scriptName

    def rowCount(self, index): 
        return len(self.scripts)
