from project.car.car import Car


class MuscleCar(Car):
    minimum_speed = 250
    maximum_speed = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not MuscleCar.minimum_speed <= value <= MuscleCar.maximum_speed:
            raise ValueError(f"Invalid speed limit! Must be between {MuscleCar.minimum_speed} and {MuscleCar.maximum_speed}!")
        self.__speed_limit = value



