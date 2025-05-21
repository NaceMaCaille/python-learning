class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    
    def get_full_name(self):
        full_name = f"Ім'я - {self.name}, Прізвище - {self.surname}"
        return full_name
    
    
    def set_full_name(self,full_name):
        self.name, self.surname = full_name.split(" ")
        
    
    def __repr__(self):
        return self.get_full_name()


class Student(Human):
    pass

person = Human("Іван", "Петренко", 30)    

print(person)

person.set_full_name("Олена Шевченко")

print(person)
