#! python 3

import sys
import os
import logging

# pyside 2
from PySide2.QtWidgets import *

# Custom Widget
from app.MainWindowWidget import MainWindowWidget

#Sets up logging
logging.basicConfig(level=logging.DEBUG, format='\t%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.ERROR) # uncomment to block debug logging.debug messages
#logging.disable(logging.DEBUG) # uncomment to block debug logging.debug messages
#logging.disable(logging.INFO) # uncomment to block debug logging.info messages and below

if __name__ == "__main__": 
    app = QApplication(sys.argv)

    w = MainWindowWidget()  
    w.show() 

    app.exec_()
    logging.info("Main:: -> EXIT: Closing window")
