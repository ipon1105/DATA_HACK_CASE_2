from Generator import Generator
from Table import Table, Column
from Config import Config

def printTable(t:Table):
    print(t.name)

    for column in t.column_array:
        print(column.name, end='\t')
        pass
    print('\n')


    l = Config.GENERAL_COUNT
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
    Product = Table("Product", [
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Manufacturer", Config.CONFIG_TYPE_STR),
        Column("Type", Config.CONFIG_TYPE_STR)
    ])

    #t2.
    PC = Table("PC", [
        Column("Code", Config.CONFIG_TYPE_INT),
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Speed", Config.CONFIG_TYPE_INT),
        Column("Memory", Config.CONFIG_TYPE_INT),
        Column("HD", Config.CONFIG_TYPE_INT),
        Column("ReadSpeed",Config.CONFIG_TYPE_INT),
        Column("Price", Config.CONFIG_TYPE_INT)
        ])

    #t3.
    Notebook = Table("Notebook", [
        Column("Code", Config.CONFIG_TYPE_INT),
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Speed", Config.CONFIG_TYPE_INT),
        Column("Memory",Config.CONFIG_TYPE_INT),
        Column("HD", Config.CONFIG_TYPE_INT),
        Column("Display", Config.CONFIG_TYPE_INT),
        Column("Price", Config.CONFIG_TYPE_INT)
        ])

    #t4.
    Printer = Table("Printer", [
        Column("Code", Config.CONFIG_TYPE_INT),
        Column("Number", Config.CONFIG_TYPE_INT),
        Column("Color", Config.CONFIG_TYPE_INT),
        Column("Type", Config.CONFIG_TYPE_STR),
        Column("Price", Config.CONFIG_TYPE_INT)
        ])

    # TODO: Должен быть отдельный файл где описывается таблицы и значения по умолчанию

    # TODO: ВЫВОД SPARKET

    # TODO: Для каждой таблицы своё количество строк

    # TODO: DOCKER = YANDEX + GOOGLE оф сайты

    gen = Generator([Product, PC, Notebook, Printer])
    gen.run()
    printTable(Product)
    printTable(PC)
    printTable(Notebook)
    printTable(Printer)