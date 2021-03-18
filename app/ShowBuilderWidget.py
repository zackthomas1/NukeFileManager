import logging

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# GUI from Qt Designer
from __QtFiles__.Widgets.showBuilder_GUI_v001 import Ui_Form

# Modules 
from modules.ShowBuilder import ShowBuilder

class ShowBuilderWidget(QWidget, Ui_Form): 
    
    showBuilder = ShowBuilder()
    
    def __init__(self, rootDirModel): 
        logging.debug("ShowBuilderWidget::__init__-> initalizing ShowBuilderWidget class")
        super().__init__() 
        self.setupUi(self)
        self.show

        # Set up data models 
        # ------------------
        self.rootDirModel = rootDirModel

        # Slot-Signal connections 
        # -----------------------
        self.CreateShow_pushButton.clicked.connect(self.call_create_show)

    def call_create_show(self): 
        inputShowCode = self.EnterShowChode_lineEdit.text()
        logging.debug("ShowBuilderWidget::call_create_show -> inputShowCode: %s" % inputShowCode)

        self.showBuilder.create_show(inputShowCode, self.rootDirModel.directory)
