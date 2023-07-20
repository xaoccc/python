import unittest

class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
   
    @property
    def make(self):
        return self.__make
   
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value
 
    @property
    def model(self):
        return self.__model
   
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value
 
    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
   
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value
 
    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
   
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value
 
    @property
    def fuel_amount(self):
        return self.__fuel_amount
   
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value
 
    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity
 
    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption
 
        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")
 
        self.__fuel_amount -= needed



        

class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("Mercedes", "CL 65 AMG", 15, 150)
        
    def test_valid_make(self):
        result = self.car.make
        expected_result = "Mercedes"
        self.assertEqual(result, expected_result)
        
    def test_valid_model(self):
        result = self.car.model
        expected_result = "CL 65 AMG"
        self.assertEqual(result, expected_result)
        
    def test_valid_fuel_consumption(self):
        result = self.car.fuel_consumption
        expected_result = 15
        self.assertEqual(result, expected_result)
        
    def test_valid_fuel_capacity(self):
        result = self.car.fuel_capacity
        expected_result = 150
        self.assertEqual(result, expected_result)
        
    def test_invalid_make(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(context.exception))
        
    def test_invalid_model(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(context.exception))
        
    def test_invalid_fuel_consumption(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))
        
    def test_invalid_fuel_capacity(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))
        
    def test_refuel_valid(self):
        self.car.refuel(69)
        result = self.car.fuel_amount
        expected_result = 69
        self.assertEqual(result, expected_result)
        
    def test_refuel_more(self):
        self.car.refuel(666)
        result = self.car.fuel_amount
        expected_result = 150
        self.assertEqual(result, expected_result)
        
    def test_refuel_invalid(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-69)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))
        
    def test_drive_valid(self):
        self.car.refuel(100)
        self.car.drive(150)
        result = self.car.fuel_amount
        expected_result = 77.5
        self.assertEqual(result, expected_result)
        
    def test_drive_invalid(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(150)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))
        

        
        
if __name__ == "__main__":
    unittest.main()
