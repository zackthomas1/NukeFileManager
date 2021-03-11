import sys
import logging
import json


class Utilities(): 
    def __init__(self):
        pass

    @staticmethod
    def save_json(json_file, data_struc): 
        """ """ 

        logging.debug("Utilities::save_json-> saving to %s" % json_file)

        with open(json_file, 'w') as file: 
            data = json.dump(data_struc, file)

    @staticmethod
    def load_json(json_file): 
        """ """ 
        logging.debug("Utilities::load_json-> ")
        
        try: 
            with open(json_file, 'r') as file: 
                data_struct = json.load(file)
            return data_struct
        except Exception: 
            logging.error("ERROR << Utiilites::load_json-> Unable to load json file.")
            return None

