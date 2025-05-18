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
        if owner.age > 18:
            self.owner = owner
        else:
            raise ValueError('Помилка! Власник неповнолітній')

         
    async def get_info(self):
        return (
            f"Бренд - {self.brand}, Модель - {self.model},"
            f"Рік створення - {self.year_creating}, Номерний знак - {self.number_plate}"
            f"\n{self.owner.name} {self.owner.age}"
            )
        
            
    def __repr__(self):
        return self.get_info()
    
try:
    person = Human('Albert', 17)
    car = Car('Bugati','Bolide',2020,'CB 0001 AA')
    car.set_owner(person)

    print(car)
except ValueError as e:
    print(e)