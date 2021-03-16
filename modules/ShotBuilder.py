import sys
import logging 
import os

# Modules
from modules.Utilities import Utilities


class ShotBuilder(): 

    def __init__(self):
        pass

    def create_shot(self, shotCode): 
        logging.debug("ShotBuilder::create_shot -> input: %s" % shotCode)