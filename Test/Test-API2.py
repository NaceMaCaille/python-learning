import sqlite3
from datetime import datetime
import pytz

# Підключення до бази даних (або створення, якщо її нема)
conn = sqlite3.connect('Test.db')
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT NOT NULL,
    date_created TEXT NOT NULL,
    edit_date TEXT,
    is_complete INTEGER DEFAULT 0,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)
''')

# Вставка стандартних категорій, якщо їх ще нема
categories_list = ['спорт', 'навчання', 'покупки', 'робота', None]
for cat in categories_list:
    if cat is not None:
        cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', (cat,))
conn.commit()

def get_time_now():
    time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
    return time_zone.strftime("%d.%m.%Y %H:%M:%S")

def createTodo(action, select_cat):
    date_now = get_time_now()

    # Знаходимо ID категорії
    if 1 <= select_cat <= 5:
        cat_name = categories_list[select_cat - 1]
        if cat_name:
            cursor.execute('SELECT id FROM categories WHERE name = ?', (cat_name,))
            category = cursor.fetchone()
            category_id = category[0] if category else None
        else:
            category_id = None
    else:
        category_id = None

    cursor.execute('''
    INSERT INTO todos (action, date_created, category_id)
    VALUES (?, ?, ?)
    ''', (action, date_now, category_id))
    conn.commit()

def editTodo(id, action, select_cat):
    date_now = get_time_now()

    if 1 <= select_cat <= 5:
        cat_name = categories_list[select_cat - 1]
        if cat_name:
            cursor.execute('SELECT id FROM categories WHERE name = ?', (cat_name,))
            category = cursor.fetchone()
            category_id = category[0] if category else None
        else:
            category_id = None
    else:
        category_id = None

    cursor.execute('''
    UPDATE todos
    SET action = ?, edit_date = ?, category_id = ?
    WHERE id = ?
    ''', (action, date_now, category_id, id))
    conn.commit()
    return cursor.rowcount > 0

def removeTodo(id):
    cursor.execute('DELETE FROM todos WHERE id = ?', (id,))
    conn.commit()
    return cursor.rowcount > 0

def completeTodo(id, complete):
    cursor.execute('''
    UPDATE todos
    SET is_complete = ?
    WHERE id = ?
    ''', (int(complete), id))
    conn.commit()
    return cursor.rowcount > 0

def countTodo(action, select_category):
    if 1 <= select_category <= 5:
        select_cat = select_category
    else:
        print("Категорію не обрано")
        select_cat = None

    for _ in range(action):
        it = input("Нагадування - ")
        createTodo(it, select_cat)
    return True

def sortNameTodo():
    cursor.execute('''
    SELECT todos.id, todos.action, todos.date_created, todos.is_complete, categories.name
    FROM todos
    LEFT JOIN categories ON todos.category_id = categories.id
    ORDER BY todos.action
    ''')
    for row in cursor.fetchall():
        print(row)

def sortDateTodo():
    cursor.execute('''
    SELECT todos.id, todos.action, todos.date_created, todos.is_complete, categories.name
    FROM todos
    LEFT JOIN categories ON todos.category_id = categories.id
    ORDER BY todos.date_created DESC
    ''')
    for row in cursor.fetchall():
        print(row)

def getTodolist():
    cursor.execute('''
    SELECT todos.id, todos.action, todos.date_created, todos.is_complete, categories.name
    FROM todos
    LEFT JOIN categories ON todos.category_id = categories.id
    ''')
    for row in cursor.fetchall():
        print(row)

# Далі залишаємо chooseOption без великих змін
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
            print("Нагадування створено.")
        else:
            print("Помилка.")

    def completeTodo_inteface():
        todo_id = int(input("Введіть ID нагадування для помітки - "))
        print("1 - Так, виконав")
        print("2 - Ні, не виконав")
        choice = int(input("Ви виконали це нагадування - "))
        completed = choice == 1
        success = completeTodo(None, todo_id, completed)
        if success:
            print("Статус нагадування оновлено.")
        else:
            print("Нагадування не знайдено.")

    def editTodo_inteface():
        id = int(input("Введіть ID для редагування - "))
        action = input("Нове нагадування - ")
        print("1 - Спорт")
        print("2 - Навчання")
        print("3 - Покупки")
        print("4 - Робота")
        print("5 - Без категорії")
        select_cat = int(input('Змініть категорію - '))
        successEdit = editTodo(id, action, select_cat)
        if successEdit:
            print("Нагадування оновлено.")
        else:
            print("Нагадування не знайдено.")

    def removeTodo_inteface():
        id = int(input("Введіть ID нагадування для видалення - "))
        successRemove = removeTodo(id)
        if successRemove:
            print("Нагадування видалено.")
        else:
            print("Помилка видалення.")

    option = {
        '1': countTodo_inteface,
        '2': editTodo_inteface,
        '3': removeTodo_inteface,
        '4': sortNameTodo,
        '5': sortDateTodo,
        '6': completeTodo_inteface,
        '7': getTodolist,
        '0': exit
    }

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
            print("Помилка вибору.")

chooseOption()

# Важливо закрити підключення до бази при виході
conn.close()
