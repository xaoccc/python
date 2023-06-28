class Vehicle():
    DEFAULT_FUEL_CONSUMPTION = 1.25
    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power
        
    def drive(self, kilometers):
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= (kilometers * self.fuel_consumption)
