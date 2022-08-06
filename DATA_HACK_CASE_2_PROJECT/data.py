from Table import Table, Column
from Config import Config


class data:
    # t1.
    Product = Table("Product", [
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Manufacturer", Config.CONFIG_TYPE_STR),
        Column("Type", Config.CONFIG_TYPE_STR)
    ])

    # t2.
    PC = Table("PC", [
        Column("Code", Config.CONFIG_TYPE_INT),
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Speed", Config.CONFIG_TYPE_INT),
        Column("Memory", Config.CONFIG_TYPE_INT),
        Column("HD", Config.CONFIG_TYPE_INT),
        Column("ReadSpeed", Config.CONFIG_TYPE_INT),
        Column("Price", Config.CONFIG_TYPE_INT)
    ])

    # t3.
    Notebook = Table("Notebook", [
        Column("Code", Config.CONFIG_TYPE_INT),
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Speed", Config.CONFIG_TYPE_INT),
        Column("Memory", Config.CONFIG_TYPE_INT),
        Column("HD", Config.CONFIG_TYPE_INT),
        Column("Display", Config.CONFIG_TYPE_INT),
        Column("Price", Config.CONFIG_TYPE_INT)
    ])

    # t4.
    Printer = Table("Printer", [
        Column("Code", Config.CONFIG_TYPE_INT),
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Color", Config.CONFIG_TYPE_INT),
        Column("Type", Config.CONFIG_TYPE_STR),
        Column("Price", Config.CONFIG_TYPE_INT)
    ])
