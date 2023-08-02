from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_HORSE_SPEED = 140
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)


    def train(self):
        if self.speed + 3 > 140:
            self.speed = 140
        else:
            self.speed += 3