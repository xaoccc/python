from project.vehicles.base_vehicle import BaseVehicle

class PassengerCar(BaseVehicle):
    def __init__(self, brand, model, license_plate_number, max_mileage=450.00):
        super().__init__(brand, model, license_plate_number, max_mileage)

    
    def drive(self, mileage: float):
        self.battery_level -= int((self.battery_level * (mileage / self.max_mileage)))