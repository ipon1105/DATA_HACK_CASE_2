from dataclasses import dataclass

'''
    This python script describes a table    
    for which synthetic data will be generated. 
    The description of the table structure is a dataclass.
'''

@dataclass
class Column:
    "The class denotes a database column"

    # The name field describes the column name
    name: str

    # The type field describes one of the possible column types
    type: int

    pass

@dataclass
class Table:
    "The class denotes a database table"

    # The name field describes the table name
    name: str

    # The primary_index field describes the primary field index
    primary_index: int

    # The column_array field describes array of Column elements
    column_array: list[Column]
    pass
