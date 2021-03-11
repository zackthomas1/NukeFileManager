import sys
import logging 
import subprocess 
import os

class ShotBrowser(): 
    
    # Instant Variables
    rootDir = ""
    showCode = ""
    shotCode = ""
    shotScriptsDir = ""

    scriptFiles = []

    exePath = "C:\\Program Files\\Nuke12.2v5\\Nuke12.2.exe --indie"   
    
    def __init__(self): 
        pass
  
    def launch_nukeindie(self, scriptName = None): 
        """Launches an instance of nuke indie application"""   

        if scriptName != None:
            nkScript = os.path.join(self.shotScriptsDir, scriptName)
            subprocess.Popen("%s %s" % (self.exePath, nkScript))
            logging.debug("FileManger::launch_nukeindie->launching nuke nkScript: \'%s\'" % nkScript)
        else: 
            subprocess.Popen(self.exePath)
            logging.debug("FileManger::launch_nukeindie-> launching nuke")
        
    def set_root_dir(self, inputDirPath):
        """ """
        
        if os.path.isdir(inputDirPath): 
            self.rootDir = inputDirPath
            logging.debug ("ShotBrowser::set_root_dir-> pathDirName: %s" % self.rootDir)
        else: 
            logging.error("ERROR << ShotBrowser::set_root_dir-> '%s' is not valid path" % inputDirPath)
            raise Exception

    def set_show_code(self, inputShowCode): 
        """ """ 
        if os.path.isdir(os.path.join(self.rootDir, inputShowCode)):
            self.showCode = inputShowCode 
            logging.debug ("ShotBrowser::set_show_code-> showCode: %s" % self.showCode)
        else: 
            logging.error("ERROR << ShotBrowser::set_show_code-> '%s' not vaild path" % os.path.join(self.rootDir, inputShowCode))
            raise Exception

    def set_shot_code(self, inputShotCode):  
        
        self.shotCode = inputShotCode
        logging.debug("ShotBrowser::set_shot_code-> shotCode: %s" % self.shotCode)

    def get_shows_list(self): 
        """Returns a list of shows in the root directory"""

        showsDir = self.rootDir
        logging.debug("ShotBrowser:::get_shows_list-> Searching dir: %s" % showsDir)

        showsList = os.listdir(showsDir)

        # Remove any folder with "_sample_" syntax these are templates for other folder/development folders 
        for show in showsList: 
            if show.startswith("_") and show.endswith("_"):
                logging.debug("ShotBrowser::get_shows_list-> removed '%s' for showsList" % show)
                showsList.remove(show) 

        logging.debug("ShotBrowser::get_shows_list-> returned %s" % str(showsList))
        return showsList

    def get_shots_list(self):
        """Returns a list of shots in show directory scripts folder""" 

        scriptsDir = os.path.join(self.rootDir, 
                                    os.path.join(self.showCode, "Scripts"
                                                )
                                )
        logging.debug("ShotBrowser:::get_shots_list-> Searching dir: %s" % scriptsDir)

        shotsList = os.listdir(scriptsDir)

        # Remove any folder with "_sample_" syntax these are templates for other folder/development folders
        for shot in shotsList: 
            if shot.startswith("_") and shot.endswith("_"): 
                logging.debug("ShotBrowser::get_shots_list-> removed '%s' for shotsList" % shot)
                shotsList.remove(shot)     

        logging.debug("ShotBrowser::get_shots_list-> returned %s" % str(shotsList))
        return shotsList

    def update_shotList(self): 
        """Takes instance variables(rootDir, showCode, shotCode) returns data structure
            to be displayed in nkFiles_listView """
        

        self.shotScriptsDir = os.path.join(self.rootDir, 
                                os.path.join(self.showCode, 
                                            os.path.join("Scripts", self.shotCode)
                                            )
                                ) 
        logging.debug("ShotBrowser::update_shotList-> shotPath: %s" % self.shotScriptsDir)
        
        self.scriptFiles = os.listdir(self.shotScriptsDir) 
        logging.debug("ShotBrowser::update_shotList-> return: %s" % str(self.scriptFiles))

        return self.scriptFiles

    def doubleClick_launch_script_nukeIndie(self, scriptName): 
        """Opens selected script with instance of nuke indie"""

        nkScript = os.path.join(self.shotScriptsDir, scriptName)
        logging.debug("ShotBrowser::doubleClick_launch_script_nukeIndie-> nkScript: \'%s\'" % nkScript)

        subprocess.Popen("%s %s" % (self.exePath, nkScript))

