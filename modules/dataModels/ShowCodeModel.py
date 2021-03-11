import sys, logging

from PySide2.QtCore import * 
from PySide2.QtGui import * 
from PySide2.QtWidgets import * 

class ShowCodeModel(QAbstractListModel): 

    def __init__(self, shows = None):
        super().__init__()
        self.shows = shows or []
        logging.debug("ShowCodeModel::__init__ -> Initializing show code model")

    def data(self, index, role): 
        if role == Qt.DisplayRole: 

            showName = self.shows[index.row()]
            return showName

    def rowCount(self, index): 
        return len(self.shows)

