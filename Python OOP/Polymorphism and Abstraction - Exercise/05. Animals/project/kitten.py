from project.cat import Cat


class Kitten(Cat):
    def __init__(self, age, name, gender="Female"):
        super().__init__(age, name, gender)

    def make_sound(self):
        return "Meow"



