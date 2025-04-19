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
    for iteration in range(1,int(num_of_reminders)):
        action = input("Нагадування - ")
        date = input("Дата - ")
        Get_list = CreateTodo(iteration,action,date)
        saved_list.append(Get_list)

for l in saved_list:
    print(l)

s = input()

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

for r in saved_list:
    print(r)





