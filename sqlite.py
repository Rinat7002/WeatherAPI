import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('database.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')


    base.execute('CREATE TABLE IF NOT EXISTS data(city_name TEXT, Weather TEXT)')
    base.commit()

def sql_add(city, result):
    cur.execute('INSERT INTO data VALUES (?, ?)', tuple((city, result)))
    base.commit()