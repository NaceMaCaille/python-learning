from datetime import datetime
import pytz
import sqlite3

with sqlite3.connect("API Database.db") as con:
    cur = con.cursor()

    cur.executescript("""
        CREATE TABLE IF NOT EXISTS todo(  
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            date INTEGER,
            category TEXT,
            is_complete INTEGER,
            edit_date INTEGER,
            FOREIGN KEY (category) REFERENCES categories(id)
            );
        CREATE TABLE IF NOT EXISTS category(
            id INTEGER PRIMARY KEY,
            categories TEXT          
        )
        """)




time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
formated = time_zone.strftime("%d.%m.%Y %H:%M:%S")

def chooseOption():
    def countTodo_inteface():
        action = int(input("Кількість нагадувань - "))

        print("1 - Cпорт")
        print("2 - Навчання")
        print("3 - Покупки")
        print("4 - Робота")
        print("5 - Без категорії")

        select_category = int(input("Оберіть категорію нагадувань - "))

        success = countTodo(action,select_category)

        if success:
            print("Статус нагадування оновлено.")
        else:
            print("Erorr")

    def completeTodo_inteface(): #Complete
        todo_id = int(input("Введіть ID нагадування для помітки - "))
        print("1 - Так, виконав")
        print("2 - Ні, не виконав")
        choice = int(input("Ви виконали це нагадування - "))

        completed = choice == 1

        success = completeTodo(todo_list,todo_id,completed)
        
        if success:
            print("Статус нагадування оновлено.")
        else:
            print("Нагадування з таким ID не знайдено.")
        
    def editTodo_inteface(): #Edit
        id = int(input("Введіть ID для редагування - "))

        action = input("Нове нагадування - ")
            
        print("1 - Cпорт")
        print("2 - Навчання")
        print("3 - Покупки")
        print("4 - Робота")
        print("5 - Без категорії")
            
        select_cat = int(input('Змініть категорію - '))

        success_edit = editTodo(id,action,select_cat)
        if success_edit:
            print("Нагадування оновлено.")
        else:
            print("Нагадування з таким ID не знайдено.")

    def removeTodo_inteface(): #Remove
        id = int(input("Введіть ID нагадування для видалення - "))

        successRemove = removeTodo(id)

        if successRemove:
            print("Нагадування видалено.")
        else:
            print("Erorr")
    
    
    option = {
    '1':countTodo_inteface,
    '2':editTodo_inteface,
    '3':removeTodo_inteface,
    '4':sortNameTodo,
    '5':sortDateTodo,
    '6':completeTodo_inteface,
    '7':getTodolist,
    '0':exit
    }

    print("1 - Створити нагадування")
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
        print("4 - Сортувати за назвою")
        print("5 - Сортувати за датою")
        print("6 - Помітити нагадування")
        print("7 - Показати всі нагадування")
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


def countTodo(count,category): # Count
    todos = []
    for _ in range(count):
        action = input("Нагадування - ")
        todos.append(action)
        create_todo(todos[-1],category)

def editTodo(id,action,select_cat): # Edit
    pass

def removeTodo(id): # Clear
    pass


def completeTodo(todo_list,id,complete): # Complete todo
   pass
            
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
    except ValueError:
        print("erorr")
    finally:
        cur.close()
        sql_connection.close()
        
    
    
chooseOption()


