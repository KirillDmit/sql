import sqlite3
from pprint import pprint


def dict_factory(cursor, row):
    # обертка для преобразования
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


con = sqlite3.connect('works.sqlite')

con.row_factory = dict_factory

res = con.execute('select * from works limit 3')

pprint(list(res))

