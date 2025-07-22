import json

from utils import Todo, TodoManager
from db_utils import (sort_date_todo, sort_name_todo, get_todo_list)

def choose_option():
    with open("lib.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    categories = data["category"]
    start_comands = data["start_comands"]
    complete_text = data["complete"]
    sort = data["sort"]
    
    def create_interface():
        iteration = int(input("Кількість нагадувань - "))
        for key, value in categories.items():
            print(f"{key} - {value}")
        
        category = int(input("Категорія нагадуваь - "))
        
        for _ in range(iteration):
            text = input("Нагадування - ")
            todo = Todo(text, category)
            todo.create_todo()
    
    def edit_interface():
        id = int(input("Оберіть ID для редагуання нагадування - "))
        edit_todo = input("Нагадування - ")
        
        for key, value in categories.items():
            print(f"{key} - {value}")
        edit_category = int(input("Оберіть нову категорію - "))
        todo_edit = TodoManager(id, edit_todo, edit_category)
        todo_edit.edit_todo()
        
    def remove_interface():
        id_ = int(input("Оберіть ID для видалення нагадування - "))
        remove = TodoManager(id=id_)
        remove.remove_todo()
        print("Нагадування видалено!")
        
    def complete_interface():
        id_ = int(input("Оберіть ID для помітки нагадування - "))
        for key, value in complete_text.items():
            print(f"{key} - {value}") 
        choice = int(input("Ви виконали це нагадування - "))
        complete = TodoManager(id=id_, is_complete=choice)
        complete.complete_todo()
        
    def sort_date_interface():
        for key, value in sort.items():
            print(f"{key} - {value}")
        type_ = int(input("Оберіть тип сорутування - "))
        sort_date_todo(type_)
        
    def sort_name_interface():
        for key, value in sort.items():
            print(f"{key} - {value}")
        type_ = int(input("Оберіть тип сорутування - "))
        sort_name_todo(type_)
            
    options = {
        1: create_interface,
        2: edit_interface,
        3: remove_interface,
        4: complete_interface,
        5: sort_date_interface,
        6: sort_name_interface,
        7: get_todo_list,
        0: exit
    }
    
    while True:
        for key, value in start_comands.items():
            print(f"{key} - {value}")
            
        get = int(input("Оберіть опцію - "))
        
        choose_comand = options.get(get)
        
        if choose_comand:
            choose_comand()
        else:
            ("Такої команди не існує")