import random
import json

from Table import ColumnRules

'''
    This python script describes a Configuration information
'''

class Config:

    # The default types of data
    CONFIG_TYPE_0 = CONFIG_TYPE_INT         = int(0)  #int
    CONFIG_TYPE_1 = CONFIG_TYPE_STR         = int(1)  #string
    CONFIG_TYPE_2 = CONFIG_TYPE_FLOAT       = int(2)  #float
    CONFIG_TYPE_3 = CONFIG_TYPE_DATE        = int(3)  #date
    CONFIG_TYPE_4 = CONFIG_TYPE_TIMESTAMP   = int(4)  #timestamp

    # Base Constucter
    def __init__(self):
        # self.conf - information from configuration
        self.conf = None

    # Read JSON file
    def read(self):
        with open("data.json") as d:
            self.conf = json.load(d)
        pass

    def getConf(self, confName):
        return self.conf[confName]


    # Count of rows to generator
    FIELD_COUNT = int(100)

    # RANDOM_SEED to randomize the massive of data
    # RANDOM_SEED = 100

    # Language to localization the massive of data
    # LOCALIZATION = str("ru_RU")

    # Minimal year of age
    # MIN_YEAR_AGE = str("-30y")

    # Maximum year of age
    # MAX_YEAR_AGE = str("-20y")

    # Start years of live
    # START_YEAR = str("-30y")

    # JOIN_INDEX_ARR = list()

    # Mobile phone
    # PHONE = int(80237391431)

    # Range of numbers
    # NUMBER_RANGE = [[-50,150],[30,100]]

    # Fixed range for string or not
    # STRING_FIXED = true

    # Minimal count of character
    # STRING_MIN = 5

    # Maximum count of character
    # STRING_MAX = 100

    # Minimal value of timestamp
    # TIMESTAMP_MIN = 20020511235859

    # Maximum value of timestamp
    # TIMESTAMP_MAX = 20220511235859

    # Templates to numbers
    # NUMBER_TEMPLATES = [960, 1080, 1280, 1920]

    # Templates to strings and characters
    # STRING_TEMPLATES = ["CODEX","RUNNER","GUN"]

    # Mask for a String
    # STRING_MASK = "My_P#in_is_*"

    # Mask for integer
    # NUMBER_MASK = "202#*"
