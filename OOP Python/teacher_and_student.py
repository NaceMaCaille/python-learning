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
        for student in self.students:
            if student.name == name:
                return student
        return None


    def remove_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return self.students.remove(student)
        return None


    def update_student_by_name(self, replace_student, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return self.students.append(replace_student)
        return None


    def find_cheater_student(self):
        for student in self.students:
            avg_real = sum(student.marks) // len(student.marks)
            avg_curent = student.get_average_mark()
            if avg_curent != avg_real:
                return f"{student.get_full_name()}"
        return None


class FakeStudent(Student):
    def __init__(self, name, surname, age, marks):
        super().__init__(name, surname, age, marks)

        self.__cheated_marks = self.cheat()

    def cheat(self):
        return [min(mark * 2, 10) for mark in self.marks]


    def get_average_mark(self):
        return sum(self.__cheated_marks) // len(self.__cheated_marks)


    def get_min_mark(self):
        return min(self.__cheated_marks)


    def get_max_mark(self):
        return max(self.__cheated_marks)


ivan = Student("Іван", "Петренко", 24,[4, 8, 3, 2, 1])
albert = Student("Альберт", "Мішустін", 25, [5, 10, 11, 3, 1])
irina = Student("Ірина", "Шевченко", 21, [10, 1, 4, 1, 7])
daria = Student("Дар'я", "Коваленко", 23, [1, 10, 1, 3, 6])
oleg = Student("Олег", "Кравчук", 22, [10, 2, 1, 4, 3])

anton = FakeStudent("Антон","Коваль", 22, [5, 2, 3, 4, 6])



student_group = [ivan, albert, irina, daria, anton]

teacher = Teacher(student_group)

print(anton.cheat())

print(
     f"Студент {ivan.get_full_name()}",
     "має середню оцінку",
     ivan.get_average_mark())

print(f"Студент {anton.get_full_name()}",
     "має середню оцінку",
     anton.get_average_mark())

print(teacher.find_cheater_student())

print(
    f"У студента {teacher.find_cheater_student()} завищені оцінки"
)