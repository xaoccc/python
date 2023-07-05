from project.cat import Cat


class Kitten(Cat):
    def __init__(self, age, name, gender):
        super().__init__(age, name, gender="Female")

    def make_sound(self):
        return "Meow"

