class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}, {self.age} років"
    
    
class Car(Human):
    def __init__(self,brand,model,year_creating,number_plate):
        self.brand = brand
        self.model = model
        self.year_creating = year_creating
        self.number_plate = number_plate
        self.owner = None
    
    def set_owner(self, owner):
        self.owner = owner
        
    def __str__(self):
        owner_info = self.owner
        return f"Бренд - {self.brand}, Модель - {self.model},Рік створення - {self.year_creating}, Номерний знак - {self.number_plate}\nВласник - {owner_info}"


person = Human("Albert", 20)
car = Car('Bugati','Bolide',2020,'CB 0001 AA')
car.set_owner(person)

print(car)