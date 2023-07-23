from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > 140:
            raise ValueError("Horse speed is too high!")
        self.__speed = value
    def train(self):
        if self.speed + 3 > 140:
            self.speed = 120
        else:
            self.speed += 3