from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False
    
    @property
    def brand(self):
        return self.__brand
        
    @brand.setter
    def brand(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Brand cannot be empty!")
        self.__brand = value
        
    @property
    def model(self):
        return self.__model
        
    @model.setter
    def model(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Model cannot be empty!")
        self.__model = value
        
    @property
    def license_plate_number(self):
        return self.__license_plate_number
        
    @license_plate_number.setter
    def license_plate_number(self, value):
        if len(value.strip()) == 0:
            raise ValueError("License plate number is required!")
        self.__license_plate_number = value
        
    @abstractmethod
    def drive(self, mileage: float):
        pass
    
    def recharge(self):
        self.battery_level = 100
    
    def change_status(self):
        if self.is_damaged:
            self.is_damaged = False
        else:
            self.is_damaged = True
            
    def __str__(self):
        status = "Damaged" if self.is_damaged else "OK"
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% Status: {status}"