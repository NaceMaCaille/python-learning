from datetime import datetime
import pytz
from db_utils import create_todo_in_db,edit_todo_in_db,delete_todo_in_db,complete_todo_in_db,get_todo_list

time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
formated = time_zone.strftime("%d.%m.%Y %H:%M:%S")


def create_todo(todos,cat,is_complete = 0):
    todo_data = []

    time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
    formated = time_zone.strftime("%d.%m.%Y %H:%M:%S")

    todo_data.append((todos, formated, cat, is_complete))
    save_to_db('create',todo_data)

def count_todo(count,category):
    todos = []

    for _ in range(count):
        action = input("Нагадування - ")
        todos.append(action)
        create_todo(todos[-1],category)

def edit_todo(id,action,select_cat):
    todo = []
    todo.append([id,action,select_cat])
    save_to_db('edit',todo)

def remove_todo(id):
    save_to_db('delete',id)


def complete_todo(id,complete):
   todo = []
   todo.append((id,complete))
   save_to_db('complete',todo)
            
def sortNameTodo(): 
    pass

def sortDateTodo():
    pass


    

def save_to_db(method,object):
    if (method  == 'create'):
        create_todo_in_db(method,object) 
    if (method  == 'edit'):
        edit_todo_in_db(method,object)   
    if (method  == 'delete'):    
        delete_todo_in_db(method,object)
    if (method  == 'complete'):
        complete_todo_in_db(method,object)