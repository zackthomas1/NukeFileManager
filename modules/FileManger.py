import sys
import logging 
import subprocess 
import os

class FileManger(): 
    
    # Instant Variables
    rootDir = ""
    showCode = ""
    shotCode = ""
    shotScriptsDir = ""

    exePath = "C:\\Program Files\\Nuke12.2v5\\Nuke12.2.exe --indie"   
    
    def __init__(self): 
        pass

     
    def launch_nukeindie(self): 
        """Launches an instance of nuke indie application"""   

        subprocess.Popen(self.exePath)
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

    def enter_shotinfo(self): 
        """Takes instance variables(rootDir, showCode, shotCode) returns data structure
            to be displayed in nkFiles_listView """
        
        self.shotScriptsDir = os.path.join(self.rootDir, 
                                os.path.join(self.showCode, 
                                            os.path.join("Scripts", self.shotCode)
                                            )
                                ) 
        logging.debug("FileManger::enter_shotinfo-> shotPath: " + self.shotScriptsDir)
        
        scriptFiles = os.listdir(self.shotScriptsDir) 
        logging.debug("FileManger::enter_shotinfo-> return:" + str(scriptFiles))

        return scriptFiles

    def doubleClick_launch_script_nukeIndie(self, scriptName): 
        """Opens selected script with instance of nuke indie"""

        nkScript = os.path.join(self.shotScriptsDir, scriptName)
        logging.debug("FileManger::doubleClick_launch_script_nukeIndie-> nkScript: \'" + nkScript + "\'")

        subprocess.Popen("%s %s" % (self.exePath, nkScript))
