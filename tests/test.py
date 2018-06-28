import os, sys

sys.path.append(os.path.abspath(".."))

from config import Config

conf = Config("settings.json")
settings = conf.get("settings")

print(settings["languages"])