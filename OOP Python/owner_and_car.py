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
            raise ValueError ('Помилка! Власник неповнолітній')
            

         
    def get_info(self):
        info_car = (
            f"Бренд - {self.brand}, Модель - {self.model},"
            f"Рік створення - {self.year_creating}, Номерний знак - {self.number_plate}"
            )
        if not self.owner == None:
            info_car += f"\nІм'я - {self.owner.name}, Прізвище - {self.owner.age}"
        else:
            info_car += '\nПомилка! Власник неповнолітній'
        return info_car 
            
            
        
            
    def __repr__(self):
        return self.get_info()
    
    

car = Car('Bugati','Bolide',2020,'CB 0001 AA')
person = Human('Albert', 17)

try:
    car.set_owner(person)
    print(car)
except ValueError or AttributeError as e:
    print(e)

print(car.get_info())    
    
