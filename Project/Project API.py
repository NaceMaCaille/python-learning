def CreateTodo(id, a, d):
    return {
        'id': id,
        'action':a,
        'date':d
    }
    

s = input()

if "Створити нагадування":
    saved_list = []
    num_of_reminders = input()
    for iteration in range(1,int(num_of_reminders) + 1):
        action = input("Нагадування - ")
        date = input("Дата - ")
        Get_list = CreateTodo(iteration,action,date)
        saved_list.append(Get_list)

for s_l in saved_list:
    print(s_l)

y = s

if "Редагувати нагадування":
    edit_id = int(input())
    for l in saved_list:
        if l['id'] == edit_id:
            edit_action = input('Нагадування - ')
            edit_date = input("Дата - ")
            l.update({'action':edit_action,'date':edit_date})
            break
        else:
            print("Такого id не існує")

for s_l in saved_list:
    print(s_l)

if "Видалити нагадування":
    enter_delete_list = input("Введіть")
    for delete in saved_list:
        if delete['id'] == enter_delete_list:
            delete.clear()
            break

for s_l in saved_list:
    print(s_l)





