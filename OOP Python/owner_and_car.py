class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}, {self.age} років"
    
    
class Car:
    def __init__(self,brand,model,year_creating,number_plate):
        self.brand = brand
        self.model = model
        self.year_creating = year_creating
        self.number_plate = number_plate
        self.owner = None
    
    
    def set_owner(self, owner):
        self.owner = owner
        
    def get_info(self):    
        if self.owner.age >= 18:
            return f"Бренд - {self.brand}, Модель - {self.model},Рік створення - {self.year_creating}, Номерний знак - {self.number_plate}\nВласник - {self.owner.name} {self.owner.age}"
        else:
            return "Власник неповнолітній"
    
    def __repr__(self):
        return self.get_info()

name = input("І'мя власника - ")
age = int(input("Рік народження - "))

person = Human(name, age)
car = Car('Bugati','Bolide',2020,'CB 0001 AA')
car.set_owner(person)

print(car)