import sys
import logging 
import subprocess 
import os

class FileManger(): 
    
    rootDir = ""
    showCode = ""
    shotCode = ""
    
    def __init__(self): 
        pass

    @staticmethod 
    def launch_nukeindie(): 
        """Launches an instance of nuke indie application"""

        filePath = "\"C:\\Program Files\\Nuke12.2v5\\Nuke12.2.exe\" --indie"      

        subprocess.Popen(filePath)
        logging.debug("FileManger::launch_nukeindie-> launching nuke")

    def set_root_dir(self, inputDirPath):
        """ """
        
        if os.path.isdir(inputDirPath): 
            self.rootDir = inputDirPath
            logging.debug ("FileManger::set_root_dir-> pathDirName: " + self.rootDir)
        else: 
            logging.error("ERROR<<FileManger::set_root_dir-> provided filepath " + 
                            inputDirPath + "is not valid." )
            raise Exception

    def set_show_code(self, inputShowCode): 
        """ """ 

        self.showCode = inputShowCode 
        logging.debug ("FileManger::set_show_code-> showCode: " + self.showCode)

    def set_shot_code(self, inputShotCode): 
        """ """ 

        self.shotCode = inputShotCode
        logging.debug ("FileManger::set_shot_code-> shotCode: " + self.shotCode)

    def display_shot_versions(self): 
        """Takes instance variables(rootDir, showCode, shotCode) generates data structure
            then displays it in nkFiles_listView """

        pass 