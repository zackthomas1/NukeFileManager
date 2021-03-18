import sys
import logging 
import os
import shutil

# Modules
from modules.Utilities import Utilities


class ShotBuilder(): 

    def __init__(self):
        pass

    def create_shot(self, shotCode, rootDirectory, show): 

        # make shot directory
        shotPath = os.path.join(rootDirectory, 
                                os.path.join(show, 
                                    os.path.join("Scripts", shotCode)))
        os.makedirs(shotPath)
        logging.debug("ShotBuilder::create_shot -> shotPath: '%s'" % shotPath)


        # copy template script
        templateScriptPath = os.path.join(os.getcwd(), "assets\\templateScript_v001.nk")
        destinationScriptPath = os.path.join(shotPath, "templateScript_v001.nk")
        shutil.copyfile(templateScriptPath, destinationScriptPath)
        logging.debug("ShowBuilder::create_show-> " +
                "Copied template script to show directory: " +
                "source: %s \t destination: %s" % (templateScriptPath, destinationScriptPath))