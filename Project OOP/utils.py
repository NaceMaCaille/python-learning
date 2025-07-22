import pytz
from datetime import datetime

from db_utils import (create_todo_in_db, edit_todo_in_db,
                      delete_todo_in_db, complete_todo_in_db)


time_zone = datetime.now(pytz.timezone('Europe/Kyiv'))
formated = time_zone.strftime("%d.%m.%Y %H:%M:%S")

def save_to_db(arrays, method):
    if method == 'create':
        create_todo_in_db(arrays)
    elif method == 'edit':
        edit_todo_in_db(arrays)
    elif method == 'remove':
        delete_todo_in_db(arrays)
    elif method == 'complete':
        complete_todo_in_db(arrays) 
    
    
class Todo:
    def __init__(self, todo, category, is_complete = 0,):
        self.__todo = todo 
        self.__category = category
        self.__time = formated
        self.__is_complete = is_complete
        
    def create_todo(self):
        todos = [self.__todo, self.__category, self.__time, self.__is_complete]
        save_to_db(todos, 'create')
        

class TodoManager:
    def __init__(self, id=None, todo=None, category=None, is_complete = 0):
        self.__id = id 
        self.__todo = todo
        self.__category = category
        self.__is_complete = is_complete
        
    def edit_todo(self):
        todo_edit = [self.__id, self.__todo, self.__category]
        save_to_db(todo_edit, 'edit')
        
    def remove_todo(self):
        remove = self.__id
        save_to_db(remove, "remove")
        
    def complete_todo(self):
        complete = [self.__id, self.__is_complete]
        save_to_db(complete, 'complete')    
    
            
        
        


