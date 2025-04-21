from datetime import datetime
import pytz

todo_list = []
curent_id = 1

def createTodo(action):
    time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
    formated = time_zone.strftime("%d.%m.%Y %H:%M")
    global curent_id
    
    saved_list = {
        'id': curent_id,
        'action':action,
        'date':formated
            }
    todo_list.append(saved_list)
    curent_id += 1

def editTodo():
    id = int(input("Введіть ID нагадування для редагування - "))
    action = input("Нове нагадування - ")
    for todo in todo_list:
        if todo['id'] == id:
            todo['action'] = action
            break

def removeTodo():
    id = int(input("Введіть ID нагадування для видалення - "))
    for todo in todo_list:
        if todo['id'] == id:
            todo.clear()

def countTodo():
    action = int(input("Кількість нагадувань - "))
    for _ in range(action):
        it = input("Нагадування - ")
        createTodo(it)


def sortNameTodo():
    sorted_name = sorted(todo_list, key=lambda name: name['action'])
    for sort_list_todo in sorted_name:
        print(sort_list_todo)

def sortDateTodo():
    sorted_date = sorted(todo_list, key=lambda date: date['date'])
    for sort_list_todo in sorted_date:
        print(sort_list_todo)


def getTodolist():
    for listTodo in todo_list:
        print(listTodo)
    
    
option = {
    '1':countTodo,
    '2':editTodo,
    '3':removeTodo,
    '4':sortNameTodo,
    '5':sortDateTodo,
    '6':getTodolist,
    '0':exit
}

while True:
    print("Меню")
    print("1 - Додати кілька нагадувань")
    print("2 - Редагувати нагадування")
    print("3 - Видалити нагадування")
    print("4 - Сортувати за назвою")
    print("5 - Сортувати за датою")
    print("6 - Показати всі нагадування")
    print("0 - Вихід")


    select_option = input("Оберіть опцію - ")

    command = option.get(select_option)
    if command:
        command()
    else:
        print("Erorr")