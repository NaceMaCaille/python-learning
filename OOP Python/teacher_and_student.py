class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    
    def get_full_name(self):
        full_name = f"{self.name} {self.surname}"
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
        return sum(self.marks) // len(self.marks)
    
    
    def get_min_mark(self):    
        return min(self.marks)
    
    
    def get_max_mark(self):    
        return max(self.marks)


class Teacher:
    def __init__(self,students):
        self.students = students


    def get_list_of_names_by_average_mark(self):
        return (sorted(self.students,
                       key=lambda student: student.get_average_mark(),
                       reverse=True))


    def get_student_by_name(self, name):
        pass


    def remove_student_by_name(self, name):
        pass


ivan = Student("Іван", "Петренко", 24,[4, 8, 3, 2, 1])
albert = Student("Альберт", "Мішустін", 25, [5, 10, 11, 3, 1])
irina = Student("Ірина", "Шевченко", 21, [10, 1, 4, 1, 7])
daria = Student("Дар'я", "Коваленко", 23, [1, 10, 1, 3, 6])

student_group = [ivan, albert, irina, daria]

lidia = Teacher(student_group)
print(lidia.get_list_of_names_by_average_mark())

print(
     f"Студент {ivan.get_full_name()}",
     "має середню оцінку",
     ivan.get_average_mark()
   )




