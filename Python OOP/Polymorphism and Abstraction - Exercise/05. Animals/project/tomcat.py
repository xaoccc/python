from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, age, name, gender="Male"):
        super().__init__(age, name, gender)

    def make_sound(self):
        return "Hiss"



