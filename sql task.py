import sqlite3

con = sqlite3.connect('works.sqlite')
cur = con.cursor()

res = con.execute('SELECT COUNT(*) FROM works')
print(list(res))


res = cur.execute('SELECT COUNT(*) FROM works')
for e in res:
    print(e)

res = cur.execute('SELECT COUNT(*) from works where gender = "Женский"')
for e in res:
    print(e)

res = cur.execute('SELECT COUNT(*) from works where gender = "Мужской"')
for e in res:
    print(e)

res = cur.execute('SELECT COUNT(*) from works where skills not null ')
for e in res:
    print(e)

res = cur.execute('SELECT skills from works where skills not null ')
for e in res:
    print(e)

res = cur.execute('SELECT salary from works where skills like "%Python%"')
for e in res:
    print(e)

