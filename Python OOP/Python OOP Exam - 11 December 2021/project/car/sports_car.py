from project.car.car import Car


class SportsCar(Car):
    minimum_speed = 400
    maximum_speed = 600

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if not SportsCar.minimum_speed <= value <= SportsCar.maximum_speed:
            raise ValueError(f"Invalid speed limit! Must be between {SportsCar.minimum_speed} and {SportsCar.maximum_speed}!")
        self.__speed_limit = value
        