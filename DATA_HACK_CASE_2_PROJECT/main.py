from faker import Faker

import Config
from Config import CONFIG_TYPE_STR, CONFIG_TYPE_INT
from Generator import Generator
from Table import Table, Column

if __name__ == '__main__':
    # t1.
    t1 = Table("Table_1", 0, [Column("id", CONFIG_TYPE_INT), Column("FIO", CONFIG_TYPE_STR)])

    #t2.
    t2 = Table("Table_2", 1, [Column("id", CONFIG_TYPE_INT), Column("ADDRESS", CONFIG_TYPE_STR)])

    gen = Generator([t1, t2])
    gen.run()
