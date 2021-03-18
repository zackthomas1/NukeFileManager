import sys
import logging 
import os
import shutil

# Modules
from modules.Utilities import Utilities


class ShowBuilder(): 

    def __init__(self):
        pass

    def create_show(self, showCode, rootDirectory):

        # make main show directory
        showPath = os.path.join(rootDirectory, showCode)
        os.makedirs(showPath)
        logging.debug("ShowBuilder::create_show-> " +
                "Created directory showPath: %s" % showPath)

        #show directory sub-directories
        os.makedirs(os.path.join(showPath, "Assets"))    # Assets 
        os.makedirs(os.path.join(showPath, "Footage"))   # Footage 
        os.makedirs(os.path.join(showPath, "Reference")) # Reference
        os.makedirs(os.path.join(showPath, "Renders"))   # Renders 
        os.makedirs(os.path.join(showPath, "Scripts"))   # Scripts
        os.makedirs(os.path.join(showPath, "Working"))   # Working

