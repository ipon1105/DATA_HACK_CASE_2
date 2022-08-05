import Table
import Config
#from faker import Faker

'''
    This python script describes a Generator
    which generate the massive data at table(s)
'''


import array as arr
numbers = arr.array('i',[10.0,20,30])
print(numbers)
#output
#Traceback (most recent call last):
# File "/Users/dionysialemonaki/python_articles/demo.py", line 14, in <module>
#   numbers = arr.array('i',[10.0,20,30])
#TypeError: 'float' object cannot be interpreted as an integer

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

        # Determine whether to use join
        if (True):
            pass
        else:

            for tables in self.table_arr:
                for c in tables.column_array:
                    if (c.name == "name"):
                        f
                    pass
                pass
            pass
        return None
        pass

    pass