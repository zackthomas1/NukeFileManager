import logging

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Gui
from __QtFiles__.Widgets.ShotBuilder_GUI_v001 import Ui_Form

class ShotBuilderWidget(QWidget, Ui_Form): 
    def __init__(self): 
        logging.debug("ShotBuilderWidget::__init__-> initalizing ShotBuilderWidget class")
        super().__init__() 
        self.setupUi(self)
        self.show

