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

    #Чтение из JSON
    def read(self):
        with open("data.json") as d:
            #self.conf - information from configuration
            self.conf = json.load(d)
        pass

    def get(self, info):
        table_name = info(0)
        column = info(1)
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
    # NUMBER_TEMPLATES = [[1,2,3],[5,6,7],[1,2]]

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