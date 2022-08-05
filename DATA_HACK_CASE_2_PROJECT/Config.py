import random
import json

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
        pass

    # Read JSON file
    def read(self):
        with open("data.json") as d:
            #self.conf - information from configuration
            self.conf = json.load(d)

        pass

    def getConf(self, confName):
        return self.conf[confName]

    def get(self, info):
        column = info[1]
        for t_n in self.conf["TABLES"]:
            if (info[0] == t_n):
                for c_n in self.conf['TABLES'][t_n]:
                    if (column.name == c_n):
                        match column.type:
                            case self.CONFIG_TYPE_INT:
                                for option in self.conf['TABLES'][t_n][c_n]:
                                    print(option)
                                    pass
                                #NUMBER_MASK
                                #NUMBER_TEMPLATES
                                #NUMBER_RANGE
                                pass
                            case self.CONFIG_TYPE_STR:
                                for option in self.conf['TABLES'][t_n][c_n]:
                                    print(option)
                                    pass
                                #STRING_MASK
                                #STRING_FIXED
                                #STRING_MIN
                                #STRING_MAX
                                #STRING_RANGE
                                #STRING_TEMPLATES
                                pass
                            case self.CONFIG_TYPE_FLOAT:
                                for option in self.conf['TABLES'][t_n][c_n]:
                                    print(option)
                                    pass
                                #NUMBER_MASK
                                #NUMBER_TEMPLATES
                                #NUMBER_RANGE
                                pass
                            case self.CONFIG_TYPE_DATE:
                                for option in self.conf['TABLES'][t_n][c_n]:
                                    print(option)
                                    pass
                                #TIMESTAMP_MIN
                                #TIMESTAMP_MAX
                                pass
                            case self.CONFIG_TYPE_TIMESTAMP:
                                for option in self.conf['TABLES'][t_n][c_n]:
                                    print(option)
                                    pass
                                #START_YEAR
                                #MAX_YEAR_AGE
                                #MIN_YEAR_AGE
                                pass
                        pass
                    pass
                pass
            pass
        pass
    # Count of rows to generator
    # FIELD_COUNT = int(100)

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

    # Range of character
    # STRING_RANGE = ["A","B",["C","E"]] # a, b, c - e

    # Minimal value of timestamp
    # TIMESTAMP_MIN = 20020511235859

    # Maximum value of timestamp
    # TIMESTAMP_MAX = 20220511235859

    # Templates to numbers
    # NUMBER_TEMPLATES = [960, 1080, 1280, 1920]

    # Templates to strings
    # STRING_TEMPLATES = ["CODEX","RUNNER","GUN"]

    # Mask for a String
    # STRING_MASK = "My_P#in_is_*"

    # Mask for integer
    # NUMBER_MASK = "202#*"


# Задание строк фиксированной и нефиксироанной (но ограниченной) длины из заданного диапазона символов
# Задание значений для полей типа date и timestamp из заданного диапазона
# Задание чисел и строк из заданного набора значений. Например: (123, 456, 78) или ('code_1','code_2','code_3').
# Задание диапазона значений с использованием маски для целых чисел и строк. Например, если для поля задана маска вида 123####45###, то задавать значения нужно только для позиции '#'