import sys
import logging 
import subprocess 
import os

from modules.Utilities import Utilities

class ScriptsBrowser(): 
    
    # Instant Variables
    rootDir = ""
    showCode = ""
    shotCode = ""
    shotScriptsDir = ""

    scriptList = []

    exePath = "C:\\Program Files\\Nuke12.2v5\\Nuke12.2.exe --indie" # Remove absolute path
    
    def __init__(self): 
        pass
  
    def launch_nukeindie(self, scriptName = None): 
        """Launches an instance of nuke indie application"""   

        if scriptName != None:
            nkScript = os.path.join(self.shotScriptsDir, scriptName)
            subprocess.Popen("%s %s" % (self.exePath, nkScript))
            logging.debug("ScriptsBrowser::launch_nukeindie->launching nuke nkScript: \'%s\'" % nkScript)
        else: 
            subprocess.Popen(self.exePath)
            logging.debug("ScriptsBrowser::launch_nukeindie-> launching nuke")
        
    def set_root_dir(self, inputDirPath):
        """ """
        # Files path to save json file with root directory
        jsonFile = "C:\\Dev\\Python\\PracticeProjects\\NukeFileManager\\json\\rootDirSave.json" # Remove absolute path

        if os.path.isdir(inputDirPath): 
            self.rootDir = inputDirPath
            logging.debug ("ScriptsBrowser::set_root_dir-> pathDirName: %s" % self.rootDir)
            Utilities.save_json(jsonFile, self.rootDir) # Saves root directory path to a json file
        else: 
            logging.error("ERROR << ScriptsBrowser::set_root_dir-> '%s' is not valid path" % inputDirPath)
            raise Exception

    def set_show_code(self, inputShowCode): 
        """ """ 
        if os.path.isdir(os.path.join(self.rootDir, inputShowCode)):
            self.showCode = inputShowCode 
            logging.debug ("ScriptsBrowser::set_show_code-> showCode: %s" % self.showCode)
        else: 
            logging.error("ERROR << ScriptsBrowser::set_show_code-> '%s' not vaild path" % os.path.join(self.rootDir, inputShowCode))
            raise Exception

    def set_shot_code(self, inputShotCode):  
        """ """
        
        self.shotCode = inputShotCode
        logging.debug("ScriptsBrowser::set_shot_code-> shotCode: %s" % self.shotCode)

    def update_shows_list(self, dataModel): 
        """Returns a list of shows in the root directory"""

        showsDir = self.rootDir
        logging.debug("ScriptsBrowser:::update_shows_list-> Searching dir: %s" % showsDir)
 
        dataModel.shows = os.listdir(showsDir)

        # Remove any folder with "_sample_" syntax these are templates for other folder/development folders 
        for show in dataModel.shows: 
            if show.startswith("_") and show.endswith("_"):
                logging.debug("ScriptsBrowser::update_shows_list-> removed '%s' from dataModel.shows" % show)
                dataModel.shows.remove(show) 

        logging.debug("ScriptsBrowser::update_shows_list-> returned %s" % str(dataModel.shows))
        # return dataModel.shows

    def update_shots_list(self, dataModel):
        """Returns a list of shots in show directory scripts folder""" 

        scriptsDir = os.path.join(self.rootDir, 
                                    os.path.join(self.showCode, "Scripts"
                                                )
                                )
        logging.debug("ScriptsBrowser:::update_shots_list-> Searching dir: %s" % scriptsDir)

        if os.path.isdir(scriptsDir):
            dataModel.shots = os.listdir(scriptsDir)
        else: 
            logging.error("ERROR << ScriptsBrowser::update_shots_list-> '%s' is invalid shots path" % scriptsDir)
            raise Exception

        # Remove any folder with "_sample_" syntax these are templates for other folder/development folders
        for shot in dataModel.shots: 
            if (shot.startswith("_") and shot.endswith("_")): 
                logging.debug("ScriptsBrowser::update_shots_list-> removed '%s' from dataModel.shots" % shot)
                dataModel.shots.remove(shot)     

        logging.debug("ScriptsBrowser::update_shots_list-> returned %s" % str(dataModel.shots))
        #return dataModel

    def update_scripts_list(self, dataModel): 
        """Takes instance variables(rootDir, showCode, shotCode) returns data structure
            to be displayed in nkFiles_listView """
        
        self.shotScriptsDir = os.path.join(self.rootDir, 
                                os.path.join(self.showCode, 
                                            os.path.join("Scripts", self.shotCode)
                                            )
                                )
        logging.debug("ScriptsBrowser::update_scripts_list-> shotPath: %s" % self.shotScriptsDir)

        # if user didn't set a shot code and is trying to update the scripts list
        # or didn't set the show code and is trying to update the scripts list 
        if self.shotScriptsDir.endswith("\\Scripts\\") or os.path.isdir(self.shotScriptsDir) != True: 
            logging.error("Error << ScriptsBrowser::update_scripts_list-> '%s' is not valid path to nuke scripts" % self.shotScriptsDir)
            raise Exception
        

        dataModel.scripts = os.listdir(self.shotScriptsDir) 
        
        # Remove .autosave files from list
        for script in dataModel.scripts:
            if script.endswith(".autosave") or script.endswith('~') or script.startswith("_"):
                logging.debug("ScriptsBrowser::update_scripts_list-> removed '%s' from dataModel.scripts" % script)
                dataModel.scripts.remove(script) 

        logging.debug("ScriptsBrowser::update_scripts_list-> return: %s" % str(dataModel.scripts))
        # return self.scriptList

    def doubleClick_launch_script_nukeIndie(self, scriptName): 
        """Opens selected script with instance of nuke indie"""

        nkScript = os.path.join(self.shotScriptsDir, scriptName)
        logging.debug("ScriptsBrowser::doubleClick_launch_script_nukeIndie-> nkScript: \'%s\'" % nkScript)

        subprocess.Popen("%s %s" % (self.exePath, nkScript))

