#CreateTodo = {'id': 1, 'action': 'купити продукти ', 'date': '18.04.2025.23:52'} 
#print(CreateTodo)

def CreateTodo(id, a, d):
    return {
        'id': id,
        'action':a,
        'date':d
    }

#Get_list = print(CreatrTodo(2,'посуд','19.04.2025')) 
#Get_list = print(CreatrTodo(3,'покормити кота','19.04.2025.12:00'))

s = input()

if "Get list":
    num_of_reminders = input()
    for iteration in range(1,int(num_of_reminders)):
        id = iteration
        action = input("Нагадування - ")
        date = input("Дата - ")
        Get_list = print(CreateTodo(id,action,date))
    








