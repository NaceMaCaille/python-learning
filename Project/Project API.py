#CreateTodo = {'id': 1, 'action': 'купити продукти ', 'date': '18.04.2025.23:52'} 
#print(CreateTodo)

def CreatrTodo(id, a, d):
    return {
        'id': id,
        'action':a,
        'date':d
    }

#Get_list = print(CreatrTodo(2,'посуд','19.04.2025')) 
#Get_list = print(CreatrTodo(3,'покормити кота','19.04.2025.12:00'))

s = input()

if "Get list":
    id = input('Id')
    action = input("Action")
    date = input("Date")
    Get_list = print(CreatrTodo(id,action,date))








