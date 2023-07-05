from project.cat import Cat


class Kitten(Cat):
    def __init__(self, age, name, gender):
        super().__init__(age, name, gender="Male")

    def make_sound(self):
        return "Hiss"
    