import sqlite3

con = sqlite3.connect('works.sqlite')
cur = con.cursor()
res = con.execute('select count(*) from works;')
list(res)
res = con.execute('select * from works limit 3')

for r in res:
    print(r)

for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)


