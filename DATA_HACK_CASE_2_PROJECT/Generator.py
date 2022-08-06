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

        # Transfer data from JSON to table_arr
        for table_arr_a in self.data["TABLES"]:
            for table_arr_b in self.table_arr:
                if (table_arr_a == table_arr_b.name):
                    for key_column, value_column in self.data["TABLES"][table_arr_a].items():
                        if (key_column == "COUNT"):
                            table_arr_b.count = value_column
                        else:
                            for column_arr_b in table_arr_b.column_array:
                                if (key_column == column_arr_b.name):
                                    for key, value in self.data["TABLES"][table_arr_a][key_column].items():
                                        Config.dating(self.conf, key, value, column_arr_b)

                                pass

    pass


    # A function that generates an array of data into a table(s)
    def run(self):

        # Determine whether to use join
        if (False):
            pass
        else:
            k = Config.GENERAL_COUNT
            m = 0
            while m != k:
                m+=1
                for table in self.table_arr:
                    for column in table.column_array:
                        #TODO: Для каждого столбца по необходимости предусмотреть генерацию по маске, как в функции number_holder
                        self.rabd_date(column)
                        pass
                    pass
                pass
            pass
        pass

    def rabd_date(self, column: Table.Column):
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
                    case Config.CONFIG_TYPE_FLOAT:
                        # TODO: Заменить вызов функции number_holder на соответсвующий float_holder или добавить дробную часть
                        column.row.append(self.number_holder(column))
                        pass
                    case Config.CONFIG_TYPE_STR:
                        column.row.append(self.text_holder(column))
                        pass
                pass
    pass
    # Function that generic a random text
    def text_holder(self, column: Table.Column):
        if column.rules.Mask:
            mask = column.rules.Mask

            # Эта часть отвеает за то, что бы избавиться от всех #
            # TODO: Добавить возможность заменять несколько решеток на элемент column.rules.Templates
            c_size = 0
            for c in mask:
                if c == '#':
                    c_size+=1
                elif c_size != 0:
                    k = ''
                    i = 0
                    while i !=c_size:
                        i+=1
                        k + '#'
                    self.fake.pystr(min_chars=None, max_chars=c_size)
                    mask = mask.replace(k, self.fake.text(),1)


            size = len(mask)


            if (column.rules.Range != None):
                t = column.rules.Range
                while type(t[0]) != int:
                    t = self.fake.random.choice(t)
                maxRage = self.fake.random.randint(t[0], t[1])


            max = int(maxRage[1]) if maxRage != None else column.rules.Max
            if size >= max:
                return mask
            min = maxRage[0] if maxRage != None else column.rules.Min

            prefix: str
            postfix: str

            if mask[0] == "*" and size < max:
                self.fake.pystr(min_chars=(min - size) if min >=size else 0, max_chars=max - size)
                prefix = self.fake.text()
                mask = mask.replace('*', prefix, 1)
                pass

            while mask.count('*') != 0:
                size = len(mask)
                self.fake.pystr(min_chars=(min - size) if min >= size else 0, max_chars=max - size)
                sufffix = self.fake.text()
                mask = mask.replace('*', sufffix, 1)
                pass

            return mask

        if column.rules.Fixed:
            size = column.rules.Range[1] if column.rules.Range != None else self.conf.getConf(self.conf, "STRING_MAX")
            self.fake.pystr(min_chars=0, max_chars=size)
            return self.fake.text()
            pass


        if column.rules.Templates:
            return self.fake.random.choice(column.rules.Templates)
            pass

        max = int(column.rules.Range[1]) if column.rules.Range != None else int(self.conf.getConf(self.conf, "STRING_MAX"))
        min = int(column.rules.Range[0]) if column.rules.Range != None else int(self.conf.getConf(self.conf, "STRING_MIN"))
        self.fake.pystr(min_chars=min, max_chars=max)
        return self.fake.text()
        pass

    # Function that generic a random number
    def number_holder(self, column: Table.Column):

        if (column.rules.Mask != None):
            #TODO: Добавить возможность генерировать данные из Templates и Range
            #TODO: Добавить обработку знака *
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
        else:
            t = self.conf.getConf(self.conf,"NUMBER_RANGE")
            while type(t[0]) != int:
                t = self.fake.random.choice(t)
            return self.fake.random.randint(t[0], t[1])

        return 0
        pass