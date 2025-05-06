from utils import count_todo,complete_todo,edit_todo,remove_todo

from db_utils import sort_date_todo,sort_name_todo,get_todo_list

def choose_option():
    def countodo_inteface():
        action = int(input("Кількість нагадувань - "))

        print("1 - Cпорт")
        print("2 - Навчання")
        print("3 - Покупки")
        print("4 - Робота")
        print("5 - Без категорії")

        category = int(input("Оберіть категорію нагадувань - "))

        count_todo(action,category)


    def completetodo_inteface():
        id = int(input("Введіть ID нагадування для помітки - "))
        print("1 - Так, виконав")
        print("0 - Ні, не виконав")
        choice = int(input("Ви виконали це нагадування - "))

        complete_todo(id,choice)
        
        
    def edit_todo_inteface():
        id = int(input("Введіть ID для редагування - "))

        edit_action = input("Нове нагадування - ")
            
        print("1 - Cпорт")
        print("2 - Навчання")
        print("3 - Покупки")
        print("4 - Робота")
        print("5 - Без категорії")
            
        edit_cat = int(input('Змініть категорію - '))

        edit_todo(id,edit_action,edit_cat)


    def remove_todo_inteface():
        id = int(input("Введіть ID нагадування для видалення - "))
        remove_todo(id)

    def sort_date_interface():
        print("1 - За зростанням")
        print("2 - За спаданням")
        type = input("Оберіть тип сорутування - ")
        sort_date_todo(type)
    
    def sort_name_interface():
        print("1 - За зростанням")
        print("2 - За спаданням")
        type = input("Оберіть тип сорутування - ")
        sort_name_todo(type)
    
    
    option = {
        '1': countodo_inteface,
        '2': edit_todo_inteface,
        '3': remove_todo_inteface,
        '4': completetodo_inteface,
        '5': sort_name_interface,
        '6': sort_date_interface,
        '7': get_todo_list,
        '0': exit
    }

    print("1 - Створити нагадування")
    print("2 - Редагувати існуюче нагадування")
    print("3 - Видалити нагадування")
    print("4 - Помітити нагадування")
    print('7 - Отримати існуючі нагадування')
    print("0 - Завершити програму")
    select_todo = input("Оберіть опцію - ")

    option_interface = option.get(select_todo)

    if option_interface:
        option_interface()
    else:
        print("Error")

    while True:
        print("Меню")
        print("1 - Додати кілька нагадувань")
        print("2 - Редагувати нагадування")
        print("3 - Видалити нагадування")
        print("4 - Помітити нагадування") 
        print("5 - Сортувати за назвою")
        print("6 - Сортувати за датою") 
        print("7 - Показати всі нагадування")
        print("0 - Вихід")
    
        select_option = input("Оберіть опцію - ")

        command = option.get(select_option)
        if command:
            command()
        else:
            print("Error")