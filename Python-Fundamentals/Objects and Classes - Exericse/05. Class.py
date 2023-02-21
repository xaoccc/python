class Class:
    __students_count = 22
    
    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        
    def add_student(self, student_name, grade):
        Class.__students_count -= 1
        if Class.__students_count >= 0: 
            self.students.append(student_name)
            self.grades.append(grade)
        
    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)
 
    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {Class.get_average_grade(self):.2f}"
        
#test code       
name = input()
class_name = Class(name)
class_name.add_student("Peter", 4.80)
class_name.add_student("George", 6.00)
class_name.add_student("Amy", 3.50)
print(class_name)
