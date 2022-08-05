import random
import json
'''
    This python script describes a Configuration information
'''

# The default types of data
CONFIG_TYPE_0 = CONFIG_TYPE_INT         = int(0)  #int
CONFIG_TYPE_1 = CONFIG_TYPE_STR         = int(1)  #string
CONFIG_TYPE_2 = CONFIG_TYPE_FLOAT       = int(2)  #float
CONFIG_TYPE_3 = CONFIG_TYPE_DATE        = int(3)  #date
CONFIG_TYPE_4 = CONFIG_TYPE_TIMESTAMP   = int(4)  #timestamp

# Count of rows to generator
FIELD_COUNT = int(100)

# Language to localization the massive of data
LOCALIZATION = str("ru_RU")

# Minimal year of age
# MIN_YEAR_AGE = int(18)
MIN_YEAR_AGE = str("-30y")

# Maximum year of age
# MAX_YEAR_AGE = int(26)
MAX_YEAR_AGE = str("-20y")

# Start years of live
# START_YEAR = int(0)
START_YEAR = str("-30y")

# Числа из диапозона
MIN_A = int()
MAX_B = int()
RANDOM = random.randint(MIN_A, MAX_B)

#Чтение из JSON

with open("data.json") as d:
    data_s = json.load(d)
    print(data_s)


# Задание строк фиксированной и нефиксироанной (но ограниченной) длины из заданного диапазона символов
# Задание значений для полей типа date и timestamp из заданного диапазона
# Задание чисел и строк из заданного набора значений. Например: (123, 456, 78) или ('code_1','code_2','code_3').
# Задание диапазона значений с использованием маски для целых чисел и строк. Например, если для поля задана маска вида 123####45###, то задавать значения нужно только для позиции '#'