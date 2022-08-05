import Table
import Config
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
        self.table_arr = table_arr

        for table in self.table_arr:
            for column in table.column_array:
                column.row = list()

        self.fake = Faker(Config.LOCALIZATION)
        pass

    # A function that generates an array of data into a table(s)
    def run(self):

        # Determine whether to use join
        if (False):
            pass
        else:
            for table in self.table_arr:
                for column in table.column_array:
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

        return None
        pass

    pass