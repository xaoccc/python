
class Parent:

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
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, (float, int)) or not value.isalpha() or len(value.strip()) < 2:
            raise ValueError("Last name cannot contain digits and must be at least two characters long!")
        self.__last_name = value


    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, value):
        if isinstance(value, (float, int)) or not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid ID! ID number cannot contain letters and must consist of exactly 10 digits!")
        self.__id_number = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Invalid age! Age must be an integer!")
        if not 17 < value < 91:
            raise ValueError("Invalid age! Age cannot be less than 18 or more than 90!")
        self.__age = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value not in ["male" , "female"]:
            raise ValueError("We are not that modern. Please choose between 'male' and 'female'.")
        self.__gender = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise ValueError("Invalid rating! Rating must be an integer!")
        if not -10000 <= value <= 10000:
            raise ValueError("Invalid rating! Rating cannot be less than -10000 or more than 10000!")
        self.__rating = value










test_parent = Parent("Ivan", "Ivanov", "1122334455", 34, "fmale", "Obelya", 100)

print(test_parent.gender)