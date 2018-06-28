"""
Config JSON class 
use json files for settings
"""

import json, os

class Config:

    def __init__(self, settings_file):
        self._settings = settings_file
        self._load()

    def _load(self):
        # loading file object and set settings to json object
        try:
            file_obj = open(os.path.abspath(self._settings))
            self._settings = json.loads(file_obj.read(), encoding="UTF-8")
        except Exception as e:
            print("ERROR: {}".format(e))

    def get(self, key):
        # returns None if the key wasnt found
        if not key in self._settings:
            return None

        return self._settings[key]