import sqlite3 as sq
 
with sq.connect("Testdb.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE 'games'(
        'user_id' INTEGER,
        'score' INTEGER,        
        'time' INTEGER
        )""");