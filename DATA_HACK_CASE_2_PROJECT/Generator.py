import Table
#from faker import Faker
#import Config

'''
    This python script describes a Generator
    which generate the massive data at table(s)
'''

class Generator:
    "Class for generating data to the table(s)"

    # The table_arr field describes the array of Table classes
    table_arr: list(Table)

    # Constructor that accepts an array of tables to fill in
    def __init__(self, table_arr: list(Table)):
        self.table_arr = table_arr
        pass

    # A function that generates an array of data into a table(s)
    def run(self):

        return None
        pass

    pass