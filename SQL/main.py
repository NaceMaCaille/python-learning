import sqlite3 as sq
 
with sq.connect("Testdb.db") as con:
    cur = con.cursor()

    cur.execute ("""CREATE TABLE "games" (
	    "Field1"	INTEGER,
	    "Field2"	INTEGER,
	    "Field3"	INTEGER
        """);