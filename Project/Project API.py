def CreateTodo(action, date):
    Create = {f"id": "1", "action": f"{action}", "date": f"{date}"}
    return Create
print(CreateTodo("купити продукти","18.04.2025.23:52"))