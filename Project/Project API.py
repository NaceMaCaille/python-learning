from datetime import datetime
import pytz
import sqlite3

con = sqlite3.connect('API Database.db')
cur = con.cursor()

cur.execute(""" 
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

cur.execute(""" 
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT NOT NULL,
    date_created TEXT NOT NULL,
    edit_date TEXT,
    is_complete INTEGER DEFAULT 0,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)
""")
category_list =  ['спорт', 'навчання', 'покупки', 'робота',None]
for cat in category_list:
    if cat is not None:
        cur.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)",(cat,))
con.commit()


def createTodo(action, cat):
    date = formated
    
    if 1 <= cat <= 5:
        cat_name = category_list[cat - 1]
        if cat_name:
            cur.execute("SELECT id FROM categories WHERE name = ?", (cat_name,))
            category = cur.fetchone()
            category_id = category[0] if category else None 
        else:
            category_id = None
    else:
        category_id = None

    cur.execute(""" 
    INSERT INTO todo (action, data_created, category_id)
    VALUES (?,?,?)
    """, (action,date,category_id)) 
    con.commit()

def editTodo(id,action,select_cat): # Edit
    date = formated
    
    if 1 <= cat <= 5:
        cat_name = category_list[cat - 1]
        if cat_name:
            cur.execute("SELECT id FROM categories WHERE name = ?", (cat_name,))
            category = cur.fetchone()
            category_id = category[0] if category else None 
        else:
            category_id = None
    else:
        category_id = None

    cur.execute(""" 
    UPDATE todo
    SET action = ? edit_date = ?, category_id =?
    WHERE id = ?
    """, (action,date,category_id,id)) 
    con.commit()

    return cur.rowcount > 0

def removeTodo(id): # Clear
    cur.execute('DELETE FROM todo WHERE id = ?', (id,))
    con.commit()
    return cur.rowcount > 0

def countTodo(action,select_category): # Count

    if 1 <= select_category <= 5:
        select_cat = category[select_category - 1]
    else:
        print("Категорію не обрано")
    
    for _ in range(action):
        it = input("Нагадування - ")
        createTodo(it,select_cat)

def completeTodo(todo_list,id,complete): # Complete todo
    cur.execute(""" 
    UPDATE todo
    SET is_complete = ?
    WHERE id = ?
    """, (int(complete),id))
    con.commit()
    return cur.rowcount > 0
            
def sortNameTodo(): # Sort 
    cur.execute("""
    SELECT todo.id, todo.action, todo.date_created, todo.is_complete, categories.name
    FROM todo
    LEFT JOIN catgories ON todo.category_id = categories.id
    ORDER BY todo.action
    """)
    for sort_n in cur.fetchall():
        print(sort_n)


def sortDateTodo(): # Sort
    cur.execute("""
    SELECT todo.id, todo.action, todo.date_created, todo.is_complete, categories.name
    FROM todo
    LEFT JOIN catgories ON todo.category_id = categories.id
    ORDER BY todo.date_created DESC
    """)
    for sort_d in cur.fetchall():
        print(sort_d)

def getTodolist(): # Get
    cur.execute(""" 
    SELECT todo.id, todo.action, todo.date_created, todo.is_complete, categories.name
    FROM todo 
    LEFT JOIN categories ON todo.category_id = category_id
    """)

category =  ['спорт', 'навчання', 'покупки', 'робота',None]

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

        success = countTodo(action, select_category)

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

        success = completeTodo(None,todo_id,completed)
        
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

        successEdit = editTodo(id,action,select_cat)
        if successEdit:
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
            
chooseOption()

con.close()
