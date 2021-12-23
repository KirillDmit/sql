import sqlite3

con = sqlite3.connect('works.sqlite')
cur = con.cursor()

cur.execute('CREATE TABLE works('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            ' salary INTEGER,'
            'educationType TEXT,'
            'jobTitle TEXT,'
            'qualification TEXT,'
            'gender TEXT,'
            'dateModify TEXT,'
            'skills TEXT,'
            'otherInfo TEXT'
            )

cur.execute(
'INSERT INTO works (id, salary, educationType, jobTitle, qualification, gender, dateModify, skills, otherInfo)'
'VALUES (1, 1000, "Высшее", "Специалист", "Магистр", "Мужской", "2021-04-01", "Аналитическое", "мышление") '
)

res = con.execute('SELECT COUNT(*) FROM works')
list(res)
res = con.execute('select * from works limit 3')

for r in res:
    print(r)

for row in cur.execute('SELECT * FROM stocks ORDER BY salary'):
    print(row)

