import Table
from faker import Faker
from Config import Config

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

    # Instance configuration file
    conf = Config
    data = None

    def dating(self, key, value, column: Table.Column):

        pass

    # Constructor that accepts an array of tables to fill in
    def __init__(self, table_arr, LOCALIZATION=None):
        self.data = self.conf.read(self.conf)

        for t in table_arr:
            for c in t.column_array:
                c.row = list()

        # The table_arr field describes the array of Table classes
        self.table_arr = table_arr

        # Faker init
        self.fake = Faker(self.conf.LOCALIZATION)
        Faker.seed(seed=self.conf.RANDOM_SEED)

        for table_arr_b in self.table_arr:
            for column_arr_b in table_arr_b.column_array:
                self.conf.to_def(self.conf, column_arr_b)

        # Transfer data from JSON to table_arr
        for table_arr_a in self.data["TABLES"]:
            for table_arr_b in self.table_arr:
                if (table_arr_a == table_arr_b.name):
                    for column_arr_a in self.data["TABLES"][table_arr_a]:
                        for column_arr_b in table_arr_b.column_array:
                            if (column_arr_a == column_arr_b.name):
                                for key, value in self.data["TABLES"][table_arr_a][column_arr_b.name].items():
                                    if (key == 'NUMBER_MASK' or
                                            key == 'STRING_MASK' or
                                            key == 'DATE_MASK'):
                                        column_arr_b.rules.Mask = value
                                    if (key == 'NUMBER_TEMPLATES' or
                                            key == 'STRING_TEMPLATES' or
                                            key == 'DATE_TEMPLATES'):
                                        column_arr_b.rules.Templates = value
                                    if (key == 'NUMBER_RANGE' or
                                            key == 'STRING_RANGE' or
                                            key == 'DATE_RANGE'):
                                        column_arr_b.rules.Range = value
                                    if (key == 'NUMBER_REPEAT' or
                                            key == 'STRING_FIXING' or
                                            key == 'DATE_REPEAT'):
                                        column_arr_b.rules.Flag = value
                                    if (key == 'NUMBER_MIN' or
                                            key == 'STRING_MIN' or
                                            key == 'DATE_MIN'):
                                        column_arr_b.rules.Min = value
                                    if (key == 'NUMBER_MAX' or
                                            key == 'STRING_MAX' or
                                            key == 'DATE_MAX'):
                                        column_arr_b.rules.Max = value


    # A function that generates an array of data into a table(s)
    def run(self):

        # Determine whether to use join
        if (False):
            pass
        else:
            k = Config.GENERAL_COUNT
            m = 0
            while m != k:
                m += 1
                for table in self.table_arr:
                    for column in table.column_array:
                        self.rand_date(column)





        pass

    def rand_date(self, column: Table.Column):
        match column.type:
            case Config.CONFIG_TYPE_INT:
                column.row.append(self.number_holder(column))
                pass
            case Config.CONFIG_TYPE_FLOAT:
                # TODO: Заменить вызов функции number_holder на соответсвующий float_holder или добавить дробную часть
                column.row.append(self.number_holder(column))
                pass
            case Config.CONFIG_TYPE_STR:
                column.row.append(self.text_holder(column))
                pass
        pass
        '''
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
                column.row.append( self.fake.date_between(start_date=Config.DATE_MIN, end_date=Config.DATE_MAX))
                print(column.row)
                pass
            case "VISIT":
                column.row.append(self.fake.time(pattern="%H:%M:%S"))
                print(column.row)
                pass
            case _:
                '''

    pass

    # Function that generic a random text
    def text_holder(self, column: Table.Column):
        if column.rules.Mask:
            mask = column.rules.Mask

            # Эта часть отвеает за то, что бы избавиться от всех #
            c_size = 0
            for c in mask:
                if c == '#':
                    c_size += 1
                elif c_size != 0:
                    k = ''
                    i = 0
                    while i !=c_size:
                        i+=1
                        k + '#'
                    self.fake.pystr(min_chars=None, max_chars=c_size)
                    mask = mask.replace(k, self.fake.text(), 1)
            return mask

        if column.rules.Templates:
            return self.fake.random.choice(column.rules.Templates)
            pass

        if (column.rules.Range != None):
            wordlist = column.rules.Range
            while type(wordlist[0]) != str:
                wordlist = self.fake.random.choice(wordlist)
            return self.fake.sentence(ext_word_list=wordlist)

        self.fake.pystr(min_chars=column.rules.Min, max_chars=column.rules.Max)
        return self.fake.text()
        pass

    def figure_count_in_number(self, k):
        return 1 + self.count_in_number(divmod(k, 10)) if k != 0 else 0

    def sharp_count_in_str(self, string):
        pass

    # Function that generic a random number
    def number_holder(self, column: Table.Column):
        if (column.rules.Mask != None):
            b = str(column.rules.Mask)
            while b.count('#') != 0:
                b = b.replace("#", str(self.fake.random.randint(0, 9)), 1)
            return int(b)

        '''
        if (column.rules.Templates != None):
             for t in column.rules.Templates:
                  figure_count_in_number(t)
             pass'''

        if (column.rules.Templates != None):
            return self.fake.random.choice(column.rules.Templates)

        if (column.rules.Range != None):
            t = column.rules.Range
            while type(t[0]) != int:
                t = self.fake.random.choice(t)
            return self.fake.random.randint(t[0], t[1])
        else:
            return self.fake.random_int(min=column.rules.Min, max=column.rules.Max)
        return 0
