from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race

class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @staticmethod
    def find_car(car_model, cars):
        for car in cars:
            if car.model == car_model:
                return car

    @staticmethod
    def find_driver(driver_name, drivers):
        for driver in drivers:
            if driver.name == driver_name:
                return driver

    @staticmethod
    def find_race(race_name, races):
        for race in races:
            if race.name == race_name:
                return race

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.VALID_CAR_TYPES:
            return

        if self.find_car(model, self.cars):
            raise Exception(f"Car {model} is already created!")

        self.cars.append(self.VALID_CAR_TYPES[car_type](model, speed_limit))
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.find_driver(driver_name, self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.find_race(race_name, self.races):
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        current_driver = self.find_driver(driver_name, self.drivers)
        if not current_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type not in self.VALID_CAR_TYPES or car_type not in [car.__class__.__name__ for car in self.cars]:
            raise Exception(f"Car {car_type} could not be found!")

        for i in range(len(self.cars) - 1, -1, -1):
            car = self.cars[i]
            if car.__class__.__name__ == car_type and not car.is_taken:
                car.is_taken = True

                if current_driver.car:
                    old_car = current_driver.car
                    old_car.is_taken = False
                    current_driver.car = car
                    return f"Driver {driver_name} changed his car from {old_car.model} to {current_driver.car.model}."

                if not current_driver.car:
                    current_driver.car = car
                    return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        current_driver = self.find_driver(driver_name, self.drivers)
        current_race = self.find_race(race_name, self.races)

        if not current_race:
            raise Exception(f"Race {race_name} could not be found!")

        if not current_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not current_driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if current_driver in current_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        if current_driver.car:
            current_race.drivers.append(current_driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        current_race = self.find_race(race_name, self.races)
        if not current_race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        cars = sorted([car for car in self.cars], key=lambda c: -c.speed_limit)
        result = []
        driver = None
        position = 0
        for c in cars:
            for d in self.drivers:
                if d.car == c:
                    driver = d
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {c.speed_limit}.")
            position += 1
            if position == 3:
                break
        return "\n".join(result)


