class Employee:
    min_age = 16
    max_age = 80
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @staticmethod
    def __check_age(value):
        if Employee.max_age < value:
            raise ValueError("Too old to work!")
        elif value < Employee.min_age:
            raise ValueError("Too young to work!")
        
    @property
    def age(self):
        return self.__age
        
    @age.setter
    def age(self, value):
        self.__check_age(value)
        self.__age = value

      
# Test
# employee = Employee("BaiPesho", 99)
# print(employee.age)
