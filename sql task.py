import sqlite3

con = sqlite3.connect('works.sqlite')
cur = con.cursor()

res = con.execute('SELECT COUNT(*) FROM works')
print(list(res))


