import json

import Table

'''
    This python script describes a Configuration information
'''


class Config:
    # The default types of data
    CONFIG_TYPE_0 = CONFIG_TYPE_INT = int(0)  # int
    CONFIG_TYPE_1 = CONFIG_TYPE_STR = int(1)  # string
    CONFIG_TYPE_2 = CONFIG_TYPE_FLOAT = int(2)  # float
    CONFIG_TYPE_3 = CONFIG_TYPE_DATE = int(3)  # date
    CONFIG_TYPE_4 = CONFIG_TYPE_TIMESTAMP = int(4)  # timestamp

    # Base Constucter
    def __init__(self):
        self.conf = None

    # Read JSON file
    def read(self):
        with open("data.json") as d:
            self.conf = json.load(d)

        for key, value in self.conf.items():
            if (key == "TABLES"):
                continue
            if (key == 'RANDOM_SEED'):
                self.RANDOM_SEED = self.conf['RANDOM_SEED']
            elif (key == 'LOCALIZATION'):
                self.LOCALIZATION = self.conf['LOCALIZATION']
            elif (key == 'GENERAL_COUNT'):
                self.GENERAL_COUNT = self.conf['GENERAL_COUNT']
            elif (key == 'COUNT'):
                self.COUNT = self.conf['COUNT']

        return self.conf
        pass

    # Random seed
    RANDOM_SEED = 100

    # Language to localization the massive of data
    LOCALIZATION = str("ru_RU")

    # General count of elements
    GENERAL_COUNT = 500

    # Numbers
    NUMBER_MASK = None
    NUMBER_TEMPLATES = None
    NUMBER_RANGE = None
    NUMBER_REPEAT = True
    NUMBER_MIN = 0
    NUMBER_MAX = 99999999

    # Strings
    STRING_MASK = None
    STRING_TEMPLATES = None
    STRING_RANGE = None
    STRING_FIXING = False
    STRING_MIN = 15
    STRING_MAX = 30

    # Dates
    DATE_MASK = None
    DATE_TEMPLATES = None
    DATE_RANGE = None
    DATE_REPEAT = True
    DATE_MIN = 1970
    DATE_MAX = 2022

    COUNT = GENERAL_COUNT
