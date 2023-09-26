from parent import Parent

class Child:
    def __init__(self, name, age, neighbourhood, parent, other):
        self.name = name
        self.age = age
        self.neighbourhood = neighbourhood
        self.parent = parent
        self.other = other

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, (float, int)) or not value.isalpha() or len(value.strip()) < 2:
            raise ValueError("Child name cannot be a number and must be at least two characters long!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        try:
            value < 0
        except TypeError:
            print("Child age cannot be a string!")
            return

        results = {
            isinstance(value, float): "Child age must be a whole number!",
            value < 0: "Child age must be a positive number!",
            value > 17: "Child must be under 18 years old!"
        }

        for check, error in results.items():
            if check:
                print(error)
                return

        self.__age = value

#tests
parent = Parent("Maria", "Petrova", "1234567890", 34, "female", "Obelya", 100)
child = Child("Ivancho", 3, "ewfwe", parent, ["deaf"])

print(child.age)
