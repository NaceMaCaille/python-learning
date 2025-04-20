from datetime import datetime
import pytz

todo_list = []
curent_id = 1

def CreateTodo(action):
    time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
    global curent_id
    
    saved_list = {
        'id': curent_id,
        'action':action,
        'date':time_zone
            }
    todo_list.append(saved_list)
    curent_id += 1

def getTodolist():
    return todo_list
    
CreateTodo('погладить кота')
CreateTodo('приготувати їжу')

for listTodo in getTodolist():
    print(listTodo)

