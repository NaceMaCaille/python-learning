from datetime import datetime
import pytz

todo_list = []
curent_id = 1

def createTodo(action):
    time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
    global curent_id
    
    saved_list = {
        'id': curent_id,
        'action':action,
        'date':time_zone
            }
    todo_list.append(saved_list)
    curent_id += 1

def editTodo(id,action):
    for todo in todo_list:
        if todo['id'] == id:
            todo['action'] = action
            break

def removeTodo(id):
    for todo in todo_list:
        if todo['id'] == id:
            todo.clear()

def countTodo():
    action = int(input("Кількість нагадувань - "))
    for _ in range(action):
        it = input("Нагадування - ")
        createTodo(it)

def getTodolist():
    return todo_list 

option = {
    '1':countTodo,
    '2':editTodo,
    '3':removeTodo,
}

select_option = input("Оберіть опцію - ")

command = option.get(select_option)
if command:
    command()
else:
    print("Erorr")
    

for listTodo in getTodolist():
    print(listTodo)







if option == "Створити нагадування":
   action = input("Кількість нагадувань - ")
   for it in range(1,int(action) + 1):
        it = input("Нагадування - ")
        createTodo(it)