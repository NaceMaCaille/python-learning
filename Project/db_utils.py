import sqlite3
import pytz
from datetime import datetime

def init_db():
    with sqlite3.connect("API Database.db") as sql_connection:
        cur = sql_connection.cursor()

        cur.execute("PRAGMA foreign_keys = ON;")

        cur.executescript("""
            CREATE TABLE IF NOT EXISTS choice_category(
                id INTEGER PRIMARY KEY,
                name TEXT          
            );

            CREATE TABLE IF NOT EXISTS todo(  
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                action TEXT,
                date INTEGER,
                category TEXT,
                is_complete INTEGER,
                edit_date INTEGER,
                FOREIGN KEY (category) REFERENCES choice_category(name)
            );
        """)
    
        sql_connection.commit()
        cur.close()

time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
formated = time_zone.strftime("%d.%m.%Y %H:%M:%S")

sql_connection = sqlite3.connect("API Database.db")
cur = sql_connection.cursor()

def create_todo_in_db(method,object):
    if (method  == 'create'):
        cur.executemany("INSERT INTO todo(action, date, category, is_complete) VALUES (?, ?, ?, ?)",object)
        sql_connection.commit()
        cur.close()


def edit_todo_in_db(method,object):
    if (method == 'edit'):
        id, action, category = object[0]
        cur.execute("SELECT * FROM todo WHERE id = ?",(id,))
    if cur.fetchone() is None:
        print("Not found id")
    else:            
        cur.execute("UPDATE todo SET action = ?,category = ?,edit_date = ? WHERE id = ?",(action,category,formated,id))
    sql_connection.commit()
    cur.close()


def delete_todo_in_db(method,object):
    id = object
    cur.execute("DELETE FROM todo WHERE id = ?",(id,))
    sql_connection.commit()
    cur.close()



def complete_todo_in_db(method,object):
    id, complete = object[0]
    cur.execute("UPDATE todo SET is_complete = ? WHERE id = ?",(complete,id))
    sql_connection.commit()
    cur.close()