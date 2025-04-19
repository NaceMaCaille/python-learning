def CreateTodo(id, a, d):
    return {
        'id': id,
        'action':a,
        'date':d
    }


s = input()

if "Create list":
    num_of_reminders = input()
    for iteration in range(1,int(num_of_reminders)):
        id = iteration
        action = input("Нагадування - ")
        date = input("Дата - ")
        Get_list = print(CreateTodo(id,action,date))
    Get_list1 = Get_list
    








