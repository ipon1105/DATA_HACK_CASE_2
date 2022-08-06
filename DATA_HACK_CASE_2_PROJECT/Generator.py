import Table
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


    # Constructor that accepts an array of tables to fill in
    def __init__(self, table_arr):
        # The table_arr field describes the array of Table classes
        self.conf = Config
        self.conf.read(self.conf)

        self.table_arr = table_arr
        for table in self.table_arr:
            for column in table.column_array:
                column.row = list()
        self.fake = Faker(Config.getConf(self.conf, "LOCALIZATION"))

        megaTable = self.conf.getConf(self.conf, "TABLES")
        #print(megaTable)

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




        '''
            
                if (tableConf == tableIn.name):
                    for columnConf in megaTable:
                        for columnIn in self.table_arr:


                for c_n in self.conf['TABLES'][t_n]:
                    if (column.name == c_n):
                        match column.type:
        '''
        pass

    # A function that generates an array of data into a table(s)
    def run(self):

        # Determine whether to use join
        if (False):
            pass
        else:
            for table in self.table_arr:
                for column in table.column_array:
                    self.define(table.name, column)
                    match column.name.upper():
                        case "FIO":
                            column.row.append(self.fake.name())
                            print(column.row)
                        case "CITY":
                            column.row.append(self.fake.city())
                            print(column.row)
                        case "JOB":
                            column.row.append(self.fake.job())
                            print(column.row)
                        case "EMAIL":
                            column.row.append(self.fake.email())
                            print(column.row)
                        case "PHONE_NUMBER":
                            column.row.append(self.fake.phone_number())
                            print(column.row)
                        case "USER_NAME":
                            column.row.append(self.fake.user_name())
                            print(column.row)

                        case "IP":
                            column.row.append(self.fake.ipv4())
                            print(column.row)

                        case "ID":
                            column.row.append(self.fake.id())
                            print(column.row)

                        case _:
                            print("thing is not 1, 2 or 3")
                    pass

                    '''
                    match column.type.upper():
                        case "BIRTHDAY":
                            column.row.append(self.fake.date_between(start_date=Config.MIN_YEAR_AGE, end_date=Config.MAX_YEAR_AGE))
                            print(column.row)
                        case "VISIT":
                            column.row.append(self.fake.time(pattern="%H:%M:%S"))
                            print(column.row)
                        case _:
                            print("thing is not 1, 2 or 3")
                    pass
                    '''
                pass

        pass

    def define(self, table_name: str, col: Table.Column):
        self.conf.get(self.conf, [table_name, col])
        pass
    pass