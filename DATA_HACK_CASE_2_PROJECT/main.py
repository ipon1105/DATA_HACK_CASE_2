from Generator import Generator

from data import *


def printTable(t: Table):
    print(t.name)

    for column in t.column_array:
        print(column.name, end='\t')
        pass
    print('\n')

    l = Config.GENERAL_COUNT
    r = 0
    while r != l - 1:
        r += 1
        for column in t.column_array:
            print(column.row[r], end='\t')
            pass
        print('\n')

    print("\n\n")
    pass


if __name__ == '__main__':
    # TODO: Должен быть отдельный файл где описывается таблицы и значения по умолчанию

    # TODO: ВЫВОД SPARKET

    # TODO: Для каждой таблицы своё количество строк

    # TODO: DOCKER = YANDEX + GOOGLE оф сайты

    gen = Generator([data.Product, data.PC, data.Notebook, data.Printer])
    gen.run()
    printTable(data.Product)
    printTable(data.PC)
    printTable(data.Notebook)
    printTable(data.Printer)
