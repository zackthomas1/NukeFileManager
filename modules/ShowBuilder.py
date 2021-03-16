import sys
import logging 
import os

# Modules
from modules.Utilities import Utilities


class ShowBuilder(): 

    def __init__(self):
        pass

    def create_show(self, showCode):
        logging.debug("ShowBuilder::create_show-> input: %s" % showCode)