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
        if owner.age >= 18:
            self.owner = owner
        else:
            owner = None
            
         
    def get_info(self):
        owner_info = (
            f"Власник - {self.owner.name} {self.owner.age} років"
            if self.owner
            else "Помилка! Власник неповнолітній"
        )
        return (
            f"Бренд - {self.brand}, Модель - {self.model},"
            f"Рік створення - {self.year_creating}, Номерний знак - {self.number_plate}"
            f"\n{owner_info}"
            )
        
            
    def __repr__(self):
        return self.get_info()


person = Human('Albert', 18)
car = Car('Bugati','Bolide',2020,'CB 0001 AA')
car.set_owner(person)

print(car)