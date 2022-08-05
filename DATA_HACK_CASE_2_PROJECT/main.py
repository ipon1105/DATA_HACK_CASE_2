from faker import Faker

import Config
from Config import CONFIG_TYPE_STR, CONFIG_TYPE_INT
from Generator import Generator
from Table import Table, Column

if __name__ == '__main__':
    # t1.
    Product = Table("Product", 0, [
        Column("Number", CONFIG_TYPE_INT),
        Column("Manufacturer", CONFIG_TYPE_STR),
        Column("Type", CONFIG_TYPE_STR)
    ])

    #t2.
    PC = Table("PC", 0, [
        Column("Code", CONFIG_TYPE_INT),
        Column("Number", CONFIG_TYPE_INT),
        Column("Speed", CONFIG_TYPE_INT),
        Column("Memory", CONFIG_TYPE_INT),
        Column("HD", CONFIG_TYPE_INT),
        Column("ReadSpeed", CONFIG_TYPE_INT),
        Column("Price", CONFIG_TYPE_INT)
        ])

    #t3.
    Notebook = Table("Notebook", 0, [
        Column("Code", CONFIG_TYPE_INT),
        Column("Number", CONFIG_TYPE_INT),
        Column("Speed", CONFIG_TYPE_INT),
        Column("Memory", CONFIG_TYPE_INT),
        Column("HD", CONFIG_TYPE_INT),
        Column("Display", CONFIG_TYPE_INT),
        Column("Price", CONFIG_TYPE_INT)
        ])

    #t4.
    Printer = Table("Printer", 0, [
        Column("Code", CONFIG_TYPE_INT),
        Column("Number", CONFIG_TYPE_INT),
        Column("Color", CONFIG_TYPE_INT),
        Column("Type", CONFIG_TYPE_STR),
        Column("Price", CONFIG_TYPE_INT)
        ])

    gen = Generator([Product, PC, Notebook, Printer])
    gen.run()
