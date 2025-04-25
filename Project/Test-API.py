from datetime import datetime
import pytz

todo_list = []
curent_id = 1
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
        

def createTodo(action, cat):
    global curent_id
    
    saved_list = {
        'id': curent_id,
        'action':action,
        'date':formated,
        'category':cat,
        'isComplete':False
            }
    todo_list.append(saved_list)
    curent_id += 1

def editTodo(id,action,select_cat): # Edit
    for todo in todo_list:
        if todo['id'] == id:
            todo['action'] = action
            todo.update({'editDate': formated})
            
            if 1 <= select_cat <= 5:
                todo.update({'category':category[select_cat - 1]})
                break

def removeTodo(id): # Clear
    for todo in todo_list:
        if todo['id'] == id:
            todo_list.remove(todo)

def countTodo(action,select_category): # Count

    if 1 <= select_category <= 5:
        select_cat = category[select_category - 1]
    else:
        print("Категорію не обрано")
    
    for _ in range(action):
        it = input("Нагадування - ")
        createTodo(it,select_cat)

def completeTodo(todo_list,id,complete): # Complete todo
   
    for todo in todo_list:
        if todo['id'] == id:
            todo['isComplete'] = complete
            return True
        return False
            
def sortNameTodo(): # Sort 
    sorted_name = sorted(todo_list, key=lambda name: name['action'])
    for sort_list_todo in sorted_name:
        print(sort_list_todo)

def sortDateTodo(): # Sort
    sorted_date = sorted(todo_list, key=lambda date: date['date'],reverse=True)
    for sort_list_todo in sorted_date:
        print(sort_list_todo)


def getTodolist(): # Get
    for listTodo in todo_list:
        print(listTodo)
    
    
chooseOption()


