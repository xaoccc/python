from project.car import Car

class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power) 
        self.fuel_consumption = SportCar.DEFAULT_FUEL_CONSUMPTION
  
