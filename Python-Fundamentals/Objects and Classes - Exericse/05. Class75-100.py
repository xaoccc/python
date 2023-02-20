class Class:
    __students_count = 22
    
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.grades = []
        self.average_grade = 0
        
    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count: 
            self.students.append(name)
            self.grades.append(grade)
        
    def get_average_grade(self):
        self.average_grade = sum(self.grades) / len(self.grades)
        return self.average_grade

    def __repr__(self):
        return f"The students in {self.class_name}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"

        
        
name = input()
class_name = Class(name)
class_name.add_student("Peter", 4.80)
class_name.add_student("George", 6.00)
class_name.add_student("Amy", 3.50)
print(class_name)
