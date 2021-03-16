import logging

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Gui
from __QtFiles__.Widgets.showBuilder_GUI_v001 import Ui_Form

class ShowBuilderWidget(QWidget, Ui_Form): 
    def __init__(self): 
        logging.debug("ShowBuilderWidget::__init__-> initalizing ShowBuilderWidget class")
        super().__init__() 
        self.setupUi(self)
        self.show

