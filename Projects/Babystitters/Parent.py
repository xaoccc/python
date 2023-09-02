from abc import ABC

class Parent(ABC):
    def __init__(self, first_name, last_name, id_number, age, gender, neighbourhood, rating):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.age = age
        self.gender = gender
        self.neighbourhood = neighbourhood
        self.rating = rating
        self.children = []

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, (float, int)) or not value.isalpha() or len(value.strip()) < 2:
            raise ValueError("First name cannot contain digits and must be at least two characters long!")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__first_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, (float, int)) or not value.isalpha() or len(value.strip()) < 2:
            raise ValueError("Last name cannot contain digits and must be at least two characters long!")
        self.__last_name = value






test_parent = Parent("Ivan", "Ivanov", "1122334455", 34, "male", "Obelya", 100)

print(test_parent.first_name)