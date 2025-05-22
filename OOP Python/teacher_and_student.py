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
    def __init__(self, name, surname, age, marks):
        super().__init__(name, surname, age)
        
        self.marks = marks
        
    def get_average_mark(self):
        return (f"{self.get_full_name}\n"
        f"Середня оцінка - {sum(self.marks) // len(self.marks)}")
    
    
    def get_min_mark(self):    
        return f"{self.get_full_name}\nМінімальна оцінка - {min(self.marks)}" 
    
    
    def get_max_mark(self):    
        return f"{self.get_full_name()}\nМаксимальна оцінка - {max(self.marks)}"
    
    

          
    
male_student = Student("Іван", "Петренко", 30,[10,9,8,1,10])    
print(male_student.get_average_mark())
print(male_student.get_min_mark())
print(male_student.get_max_mark())


