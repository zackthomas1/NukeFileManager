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
        self.selectShow_comboBox.setModel(self.showCodeModel)

        self.shotCodeModel = shotCodeModel

        # Slot-Signal connections 
        # -----------------------
        self.CreateShot_pushButton.clicked.connect(self.call_create_shot)

    def call_create_shot(self):

        # Shot Code input 
        inputShotCode = self.EnterShotChode_lineEdit.text()       
        logging.debug("ShotBuilderWidget::call_create_shot -> Calling ShotBuilder.create_shot" + 
                " with parameter %s" % inputShotCode)

        # Selected Show
        index = self.selectShow_comboBox.currentIndex() 
        inputShowCode = self.selectShow_comboBox.itemText(index)

        # Create shot
        self.shotBuilder.create_shot(inputShotCode, self.rootDirModel.directory, inputShowCode)
        
        # update shot code model
        self.shotCodeModel.shots.append(inputShotCode)
        self.shotCodeModel.shots.sort()
        self.shotCodeModel.layoutChanged.emit()