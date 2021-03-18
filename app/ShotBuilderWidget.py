import logging

# pyside2 
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# GUI from Qt Designer
from __QtFiles__.Widgets.ShotBuilder_GUI_v001 import Ui_Form

# modules 
from modules.ShotBuilder import ShotBuilder

class ShotBuilderWidget(QWidget, Ui_Form): 

    shotBuilder = ShotBuilder() 

    def __init__(self, rootDirModel, showCodeModel, shotCodeModel): 
        #logging.debug("ShotBuilderWidget::__init__-> initalizing ShotBuilderWidget class")
        super().__init__() 
        self.setupUi(self)
        self.show

        # Set up data models
        # ------------------------------
        # Root Directory Model
        self.rootDirModel = rootDirModel

        # Show Model
        self.showCodeModel = showCodeModel

        # Slot-Signal connections 
        # -----------------------
        self.CreateShot_pushButton.clicked.connect(self.call_create_shot)

    def call_create_shot(self): 
        inputShotCode = self.EnterShotChode_lineEdit.text()       
        logging.debug("ShotBuilderWidget::call_create_shot -> Calling ShotBuilder.create_shot" + 
                " with parameter %s" % inputShotCode)
        self.shotBuilder.create_shot(inputShotCode, self.rootDirModel.directory, 
                                        self.showCodeModel.selectedShow)
