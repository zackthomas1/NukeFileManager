import sys, logging

from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

class ShotCodeViewModel(QAbstractListModel): 
    
    def __init__(self, shots = None):
        super().__init__()
        self.shots = shots or [] 
        logging.debug("ShotCodeViewModel::__init__-> Initiating shot code model")

    def data(self, index, role): 
        if role == Qt.DisplayRole: 
            
            shotName = self.shots[index.row()]
            return shotName

    def rowCount(self, index): 
        return len(self.shots)
