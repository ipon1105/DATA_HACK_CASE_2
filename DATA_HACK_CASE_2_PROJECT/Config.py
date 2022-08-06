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

        '''
        self.NUMBER_MASK        = self.conf['NUMBER_MASK']      if self.conf['NUMBER_MASK']         != None else self.NUMBER_MASK
        self.NUMBER_TEMPLATES   = self.conf['NUMBER_TEMPLATES'] if self.conf['NUMBER_TEMPLATES']    != None else self.NUMBER_TEMPLATES
        self.NUMBER_RANGE       = self.conf['NUMBER_RANGE']     if self.conf['NUMBER_RANGE']        != None else self.NUMBER_RANGE
        self.NUMBER_REPEAT      = self.conf['NUMBER_REPEAT']    if self.conf['NUMBER_REPEAT']       != None else self.NUMBER_REPEAT
        self.NUMBER_MIN         = self.conf['NUMBER_MIN']       if self.conf['NUMBER_MIN']          != None else self.NUMBER_MIN
        self.NUMBER_MAX         = self.conf['NUMBER_MAX']       if self.conf['NUMBER_MAX']          != None else self.NUMBER_MAX

        self.STRING_MASK        = self.conf['STRING_MASK']      if self.conf['STRING_MASK']         != None else self.STRING_MASK
        self.STRING_TEMPLATES   = self.conf['STRING_TEMPLATES'] if self.conf['STRING_TEMPLATES']    != None else self.STRING_TEMPLATES
        self.STRING_RANGE       = self.conf['STRING_RANGE']     if self.conf['STRING_RANGE']        != None else self.STRING_RANGE
        self.STRING_FIXING      = self.conf['STRING_FIXING']    if self.conf['STRING_FIXING']       != None else self.STRING_FIXING
        self.STRING_MIN         = self.conf['STRING_MIN']       if self.conf['STRING_MIN']          != None else self.STRING_MIN
        self.STRING_MAX         = self.conf['STRING_MAX']       if self.conf['STRING_MAX']          != None else self.STRING_MAX

        self.DATE_MASK        = self.conf['DATE_MASK']      if self.conf['DATE_MASK']         != None else self.DATE_MASK
        self.DATE_TEMPLATES   = self.conf['DATE_TEMPLATES'] if self.conf['DATE_TEMPLATES']    != None else self.DATE_TEMPLATES
        self.DATE_RANGE       = self.conf['DATE_RANGE']     if self.conf['DATE_RANGE']        != None else self.DATE_RANGE
        self.DATE_REPEAT      = self.conf['DATE_REPEAT']    if self.conf['DATE_REPEAT']       != None else self.DATE_REPEAT
        self.DATE_MIN         = self.conf['DATE_MIN']       if self.conf['DATE_MIN']          != None else self.DATE_MIN
        self.DATE_MAX         = self.conf['DATE_MAX']       if self.conf['DATE_MAX']          != None else self.DATE_MAX
        '''
        return self.conf
        pass

    def dating(self, key, value, column):
        if (key == 'NUMBER_MASK' or
                key == 'STRING_MASK' or
                key == 'DATE_MASK'):
            column.rules.Mask = value
        if (key == 'NUMBER_TEMPLATES' or
                key == 'STRING_TEMPLATES' or
                key == 'DATE_TEMPLATES'):
            column.rules.Templates = value
        if (key == 'NUMBER_RANGE' or
                key == 'STRING_RANGE' or
                key == 'DATE_RANGE'):
            column.rules.Range = value
        if (key == 'NUMBER_REPEAT' or
                key == 'STRING_FIXING' or
                key == 'DATE_REPEAT'):
            column.rules.Flag = value
        if (key == 'NUMBER_MIN' or
                key == 'STRING_MIN' or
                key == 'DATE_MIN'):
            column.rules.Min = value
        if (key == 'NUMBER_MAX' or
                key == 'STRING_MAX' or
                key == 'DATE_MAX'):
            column.rules.Max = value
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
