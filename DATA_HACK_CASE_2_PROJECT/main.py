from faker import Faker

from Generator import Generator
from Table import Table, Column
from Config import Config

def printTable(t:Table):
    print(t.name + ":" + str(t.primary_index))

    for column in t.column_array:
        print(column.name, end='\t')
        pass
    print('\n')
    l = len(t.column_array[0].row)
    r = 0
    while r != l -1:
        r+=1
        for column in t.column_array:
            print(column.row[r], end='\t')
            pass
        print('\n')

    print("\n\n")
    pass

if __name__ == '__main__':
    # t1.
    Product = Table("Product", 0, [
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Manufacturer", Config.CONFIG_TYPE_STR),
        Column("Type", Config.CONFIG_TYPE_STR)
    ])

    #t2.
    PC = Table("PC", 0, [
        Column("Code", Config.CONFIG_TYPE_INT),
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Speed", Config.CONFIG_TYPE_INT),
        Column("Memory", Config.CONFIG_TYPE_INT),
        Column("HD", Config.CONFIG_TYPE_INT),
        Column("ReadSpeed",Config.CONFIG_TYPE_INT),
        Column("Price", Config.CONFIG_TYPE_INT)
        ])

    #t3.
    Notebook = Table("Notebook", 0, [
        Column("Code", Config.CONFIG_TYPE_INT),
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Speed", Config.CONFIG_TYPE_INT),
        Column("Memory",Config.CONFIG_TYPE_INT),
        Column("HD", Config.CONFIG_TYPE_INT),
        Column("Display", Config.CONFIG_TYPE_INT),
        Column("Price", Config.CONFIG_TYPE_INT)
        ])

    #t4.
    Printer = Table("Printer", 0, [
        Column("Code", Config.CONFIG_TYPE_INT),
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Color", Config.CONFIG_TYPE_INT),
        Column("Type", Config.CONFIG_TYPE_STR),
        Column("Price", Config.CONFIG_TYPE_INT)
        ])

    gen = Generator([Product, PC, Notebook, Printer])
    gen.run()
    printTable(Product)
    printTable(PC)
    printTable(Notebook)
    printTable(Printer)