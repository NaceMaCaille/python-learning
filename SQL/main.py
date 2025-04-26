import sqlite3 as sq

def readAva(n):
    try:
        with open(f"avas/{n}.png","rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


    
with sq.connect("cars.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        ava BLOB,
        score INTEGER
    )""")

    img = readAva(1)
    if img:
        binary = sq.Binary(img)
        cur.execute("INSERT INTO users VALUES ('Николай',?,1000)", (binary,))

    