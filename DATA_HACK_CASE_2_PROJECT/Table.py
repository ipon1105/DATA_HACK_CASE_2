from dataclasses import dataclass

'''
    This python script describes a table    
    for which synthetic data will be generated. 
    The description of the table structure is a dataclass.
'''


@dataclass
class ColumnRules:
    "The class denotes a Rules for Columns"

    Mask:       str = None
    Templates:  list = None
    Range:  list = None
    Flag:   bool = None
    Min:    int = None
    Max:    int = None

    def __init__(self):
        self.Mask = None
        self.Templates = None
        self.Range = None
        self.Flag = None
        self.Min = None
        self.Max = None
        pass

    pass


@dataclass
class Column:
    "The class denotes a database column"

    # The name field describes the column name
    name: str

    # The type field describes one of the possible column types
    type: int

    # An array of elements
    row = None

    # Template to create elements
    rules = None

    def __init__(self, name: str, type: int):
        self.name = name
        self.type = type
        self.row = list()
        self.rules = ColumnRules()
        pass

    pass


@dataclass
class Table:
    "The class denotes a database table"

    # The name field describes the table name
    name: str

    # The column_array field describes array of Column elements
    column_array: list[Column]

    # Count of elements
    count: int = None
    pass
