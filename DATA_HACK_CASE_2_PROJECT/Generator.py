import Table
import random
from Config import Config
from faker import Faker

'''
    This python script describes a Generator
    which generate the massive data at table(s)
'''

'''
        for i in self.table_arr:
            print("Table name: " + i.name + ";")
            print("Primary index: " + str(i.primary_index) + ";")
            print("Columns:")
            for j in i.column_array:
                print(j.name + "-" + str(j.type))
'''
class Generator:
    "Class for generating data to the table(s)"

    # Instanse configuration file
    conf = Config

    # Constructor that accepts an array of tables to fill in
    def __init__(self, table_arr):
        self.conf.read(self.conf)

        # The table_arr field describes the array of Table classes
        self.table_arr = table_arr
        for table in self.table_arr:
            for column in table.column_array:
                column.row = list()
        self.fake = Faker(Config.getConf(self.conf, "LOCALIZATION"))
        Faker.seed(seed=self.conf.getConf(self.conf, "RANDOM_SEED"))

        megaTable = self.conf.getConf(self.conf, "TABLES")
        

        for tableConf in megaTable:
            for tableIn in self.table_arr:
                if (tableConf == tableIn.name):
                    for columnConf in megaTable[tableConf]:
                        for columnIn in tableIn.column_array:
                            if (columnConf == columnIn.name):
                                match columnIn.type:
                                    case Config.CONFIG_TYPE_INT:
                                        columnIn.rules = Table.ColumnRules(None,None,None,None,None)

                                        try:
                                            columnIn.rules.Mask         = megaTable[tableConf][columnConf]["NUMBER_MASK"]
                                        except KeyError:
                                            pass
                                        try:
                                            columnIn.rules.Templates    = megaTable[tableConf][columnConf]["NUMBER_TEMPLATES"]
                                        except KeyError:
                                            pass
                                        try:
                                            columnIn.rules.Range        = megaTable[tableConf][columnConf]["NUMBER_RANGE"]
                                        except KeyError:
                                            pass
                                        pass
                                    case Config.CONFIG_TYPE_FLOAT:
                                        columnIn.rules = Table.ColumnRules(None,None,None,None,None)

                                        print(list(megaTable[tableConf][columnConf]))
                                        try:
                                            columnIn.rules.Mask         = megaTable[tableConf][columnConf]["NUMBER_MASK"]
                                        except KeyError:
                                            pass
                                        try:
                                            columnIn.rules.Templates    = megaTable[tableConf][columnConf]["NUMBER_TEMPLATES"]
                                        except KeyError: pass
                                        try:
                                            columnIn.rules.Range        = megaTable[tableConf][columnConf]["NUMBER_RANGE"]
                                        except KeyError: pass

                                        pass
                                    case Config.CONFIG_TYPE_STR:
                                        columnIn.rules = Table.ColumnRules(None, None, None, None, None)

                                        s = int(5)

                                        try:
                                            columnIn.rules.Mask = megaTable[tableConf][columnConf]["STRING_MASK"]
                                        except KeyError: pass
                                        try:
                                            columnIn.rules.Fixed = megaTable[tableConf][columnConf]["STRING_FIXED"]
                                        except KeyError: pass
                                        try:
                                            columnIn.rules.Templates = megaTable[tableConf][columnConf]["STRING_TEMPLATES"]
                                        except KeyError: pass
                                        try:
                                            s = megaTable[tableConf][columnConf]["STRING_MIN"]
                                        except KeyError: pass
                                        try:
                                            columnIn.rules.Range = [s, megaTable[tableConf][columnConf]["STRING_MAX"]]
                                        except KeyError: pass
                                        pass
                                    case Config.CONFIG_TYPE_TIMESTAMP:
                                        columnIn.rules = Table.ColumnRules(None, None, None, None, None)

                                        s = int(5)
                                        try:
                                            s = megaTable[tableConf][columnConf]["TIMESTAMP_MIN"]
                                        except KeyError: pass
                                        try:
                                            columnIn.rules.Range = [s, megaTable[tableConf][columnConf]["TIMESTAMP_MAX"]]
                                        except KeyError: pass

                                        pass
                                    case Config.CONFIG_TYPE_DATE:
                                        columnIn.rules = Table.ColumnRules(None, None, None, None, None)

                                        s = int(5)
                                        try:
                                            columnIn.rules.Mask = megaTable[tableConf][columnConf]["START_YEAR"]
                                        except KeyError: pass
                                        try:
                                            s = megaTable[tableConf][columnConf]["MIN_YEAR_AGE"]
                                        except KeyError: pass
                                        try:
                                            columnIn.rules.Range = [s, megaTable[tableConf][columnConf]["MAX_YEAR_AGE"]]
                                        except KeyError: pass
                                        pass
                                pass
                            pass

        for table in self.table_arr:
            for column in table.column_array:
                print(column.name)
                print("\t", column.rules.Mask if column.rules.Mask != None else str("\tNone"))
                print("\t", column.rules.Templates if column.rules.Templates != None else str("\tNone"))
                print("\t", column.rules.Range if column.rules.Range != None else str("\tNone"))
                print("\t", column.rules.Fixed if column.rules.Fixed != None else str("\tNone"))
                print("\t", column.rules.StartYear if column.rules.StartYear != None else str("\tNone"))
        pass

    # A function that generates an array of data into a table(s)
    def run(self):

        # Determine whether to use join
        if (False):
            pass
        else:
            for table in self.table_arr:
                for column in table.column_array:
                    #TODO: Для каждого столбца по необходимости предусмотреть генерацию по маске, как в функции number_holder
                    match column.name.upper():
                        case "FIO":
                            column.row.append(self.fake.name())
                            print(column.row)
                            pass
                        case "CITY":
                            column.row.append(self.fake.city())
                            print(column.row)
                            pass
                        case "JOB":
                            column.row.append(self.fake.job())
                            print(column.row)
                            pass
                        case "EMAIL":
                            column.row.append(self.fake.email())
                            print(column.row)
                            pass
                        case "PHONE_NUMBER":
                            column.row.append(self.fake.phone_number())
                            print(column.row)
                            pass
                        case "USER_NAME":
                            column.row.append(self.fake.user_name())
                            print(column.row)
                            pass
                        case "IP":
                            column.row.append(self.fake.ipv4())
                            print(column.row)
                            pass
                        case "ID":
                            column.row.append(self.fake.id())
                            print(column.row)
                            pass
                        case "BIRTHDAY":
                            column.row.append(
                            self.fake.date_between(start_date=Config.MIN_YEAR_AGE, end_date=Config.MAX_YEAR_AGE))
                            print(column.row)
                            pass
                        case "VISIT":
                            column.row.append(self.fake.time(pattern="%H:%M:%S"))
                            print(column.row)
                            pass
                        case _:
                            match column.type:
                                case Config.CONFIG_TYPE_INT:
                                    column.row.append(self.number_holder(column))
                                    pass

                            pass
                    pass
                pass
        pass


    # Function that generic a random number
    def number_holder(self, column: Table.Column):

        if (column.rules.Mask != None):
            b = str(column.rules.Mask)
            while b.count('#') != 0:
                b = b.replace("#", str(self.fake.random.randint(0,9)), 1)
            return int(b)

        if (column.rules.Templates != None):
            return self.fake.random.choice(column.rules.Templates)

        if (column.rules.Range != None):
            t = column.rules.Range
            while type(t[0]) != int:
                t = self.fake.random.choice(t)
            return self.fake.random.randint(t[0], t[1])

        # TODO: Необходимо доделать выбор по умолчанию, если он не настроен пользователем

        return -1
        pass