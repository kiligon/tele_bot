import sqlite3 as sq
from tabulate import tabulate


def sql_start():
    global base, cur
    base = sq.connect("main.db")
    cur = base.cursor()
    if base:
        print("Data base connected")
    base.execute('create table if not exists keys (key text PRIMARY KEY,game text,priсe real)')
    base.commit()

def sql_test():
    keys = [("adfkapdsfii","The Witcher 3: Wild Hunt","28.5"),("adfpiadfud","The Witcher 3: Wild Hunt","28.5"),("adfkadfadfadf","The Witcher 3: Wild Hunt","28.5"),("adfkad95fadf","Minecraft","30")]
    base.executemany("INSERT INTO  keys VALUES(?, ?, ?);", keys)
    

def sql_test_out():
    cur.execute("select game, avg(priсe), count(*) from keys group by game;")
    result = cur.fetchall()
    return tabulate(result,[["Game_title"][0], ["Price"][0], ["Count"][0]],tablefmt="fancy_grid")




sql_start()
sql_test()
