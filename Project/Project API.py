from datetime import datetime
import pytz
import sqlite3

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
        category TEXT UNIQUE,
        is_complete INTEGER,
        edit_date INTEGER,
        FOREIGN KEY (category) REFERENCES choice_category(id)
        );
        """)
    cur.execute("""
    SELECT 
    todo.id,
    todo.action,
    todo.date,
    choice_category.name AS category,
    todo.is_complete
    FROM todo
    JOIN choice_category ON todo.category = choice_category.id;
    """)
    sql_connection.commit()
    cur.close()

time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
formated = time_zone.strftime("%d.%m.%Y %H:%M:%S")

def choose_option():
    def countodo_inteface():
        action = int(input("Кількість нагадувань - "))

        print("1 - Cпорт")
        print("2 - Навчання")
        print("3 - Покупки")
        print("4 - Робота")
        print("5 - Без категорії")

        category = int(input("Оберіть категорію нагадувань - "))

        count_todo(action,category)


    def completetodo_inteface(): #Complete
        id = int(input("Введіть ID нагадування для помітки - "))
        print("1 - Так, виконав")
        print("0 - Ні, не виконав")
        choice = int(input("Ви виконали це нагадування - "))

        complete_todo(id,choice)
        
        
    def edit_todo_inteface(): #Edit
        id = int(input("Введіть ID для редагування - "))

        edit_action = input("Нове нагадування - ")
            
        print("1 - Cпорт")
        print("2 - Навчання")
        print("3 - Покупки")
        print("4 - Робота")
        print("5 - Без категорії")
            
        edit_cat = int(input('Змініть категорію - '))

        edit_todo(id,edit_action,edit_cat)


    def remove_todo_inteface(): #Remove
        id = int(input("Введіть ID нагадування для видалення - "))
        remove_todo(id)

    
    
    option = {
    '1':countodo_inteface,
    '2':edit_todo_inteface,
    '3':remove_todo_inteface,
    '4':completetodo_inteface,
    '5':sortNameTodo,
    '6':sortDateTodo,
    '7':getTodolist,
    '0':exit
    }

    print("1 - Створити нагадування")
    print("2 - Редагувати існуюче нагадування")
    print("3 - Видалити нагадування")
    print("4 - Помітити нагадування")
    print("0 - Завершити програму")
    select_todo = input("Оберіть опцію - ")

    option_interface = option.get(select_todo)

    if option_interface:
        option_interface()
    else:
        print("Erorr")



    while True:
        print("Меню")
        print("1 - Додати кілька нагадувань")
        print("2 - Редагувати нагадування")
        print("3 - Видалити нагадування")
        print("4 - Помітити нагадування") 
        print("5 - Сортувати за назвою (В РОЗРОБЦІ)")
        print("6 - Сортувати за датою (В РОЗРОБЦІ))") 
        print("7 - Показати всі нагадування (В РОЗРОБЦІ)")
        print("0 - Вихід")
    
        select_option = input("Оберіть опцію - ")


        command = option.get(select_option)
        if command:
            command()
        else:
            print("Erorr")
        



def create_todo(todos,cat,is_complete = 0):
    todo_data = []

    time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
    formated = time_zone.strftime("%d.%m.%Y %H:%M:%S")

    todo_data.append((todos, formated, cat, is_complete))
    save_to_db('create',todo_data)


def count_todo(count,category): # Count
    todos = []

    for _ in range(count):
        action = input("Нагадування - ")
        todos.append(action)
        create_todo(todos[-1],category)

def edit_todo(id,action,select_cat): # Edit
    todo = []
    todo.append([id,action,select_cat])
    save_to_db('edit',todo)

def remove_todo(id): # Delete
    save_to_db('delete',id)


def complete_todo(id,complete): # Complete todo
   todo = []
   todo.append((id,complete))
   save_to_db('complete',todo)
            
def sortNameTodo(): # Sort 
    pass

def sortDateTodo(): # Sort
    pass


def getTodolist(): # Get
    pass

def save_to_db(method,object):
    try:
        sql_connection = sqlite3.connect("API Database.db")
        cur = sql_connection.cursor()

        if (method  == 'create'):
            cur.executemany("INSERT INTO todo(action, date, category, is_complete) VALUES (?, ?, ?, ?)",object)
            sql_connection.commit()
            cur.close()

        if (method == 'edit'):
            id, action, category = object[0]
            cur.execute("SELECT * FROM todo WHERE id = ?",(id,))
            if cur.fetchone() is None:
                print("Not found id")
            else:            
                cur.execute("UPDATE todo SET action = ?,category = ?,edit_date = ? WHERE id = ?",(action,category,formated,id))
                sql_connection.commit()
                cur.close()

        if (method == 'delete'):
            id = object
            cur.execute("DELETE FROM todo WHERE id = ?",(id,))
            sql_connection.commit()
            cur.close()

        if (method == 'complete'):
            id, complete = object[0]
            cur.execute("UPDATE todo SET is_complete = ? WHERE id = ?",(complete,id))
            sql_connection.commit()
            cur.close()
            
    except ValueError:
        print("erorr")
    finally:
        cur.close()
        sql_connection.close()
        
    
    
choose_option()


