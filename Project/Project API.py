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
            todo_list.remove(todo)

def getTodolist():
    return todo_list 

createTodo('погладить кота')
createTodo('приготувати їжу')
editTodo(1,'погладить собаку')
removeTodo(2)

for listTodo in getTodolist():
    print(listTodo)
