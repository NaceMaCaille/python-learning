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
                category TEXT,
                date INTEGER,
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

def create_todo_in_db(arrays):
    action, category, date, is_complete = arrays
    cur.executemany("INSERT INTO todo(action, category, date, is_complete) VALUES (?, ?, ?, ?)", [(action, category, date, is_complete)])
    sql_connection.commit()
        

def edit_todo_in_db(arrays):
    id_, action, category = arrays
    cur.execute("SELECT * FROM todo WHERE id = ?",(id_,))
    if cur.fetchone() is None:
        print("Not found id")
    else:            
        cur.execute("UPDATE todo SET action = ?,category = ?,edit_date = ? WHERE id = ?",(action,category,formated,id_))
    sql_connection.commit()
    

def delete_todo_in_db(arrays):
    id = arrays
    cur.execute("DELETE FROM todo WHERE id = ?",(id,))
    sql_connection.commit()


def complete_todo_in_db(arrays):
    id, complete = arrays
    cur.execute("UPDATE todo SET is_complete = ? WHERE id = ?",(complete,id))
    sql_connection.commit()
    
    
def get_todo_list():
    cur.execute("SELECT * FROM todo;")
    todos = cur.fetchall()
    [print(todo) for todo in todos]
    sql_connection.commit()
    
def sort_name_todo(type):
    if type == 1:
        cur.execute("SELECT * FROM todo ORDER BY action ASC")
    if type == 2:
        cur.execute("SELECT * FROM todo ORDER BY action DESC")
    todos_sort_name = cur.fetchall()
    [print(todo) for todo in todos_sort_name]
    sql_connection.commit()
    
def sort_date_todo(type):
    if type == 1:
        cur.execute("SELECT * FROM todo ORDER BY date ASC")
    if type == 2:
        cur.execute("SELECT * FROM todo ORDER BY date DESC")
    todos_sort_date = cur.fetchall()
    [print(todo) for todo in todos_sort_date]
    sql_connection.commit()
    