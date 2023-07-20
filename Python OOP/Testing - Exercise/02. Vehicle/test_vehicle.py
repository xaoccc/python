import unittest
from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(33.5, 150.6)
        
    def test_fuel(self):
        result = self.vehicle.fuel
        expected_result = 33.5
        self.assertEqual(result, expected_result)
        
    def test_horse_power(self):
        result = self.vehicle.horse_power
        expected_result = 150.6
        self.assertEqual(result, expected_result)
        
    def test_DEFAULT_FUEL_CONSUMPTION(self):
        result = self.vehicle.DEFAULT_FUEL_CONSUMPTION
        expected_result = 1.25
        self.assertEqual(result, expected_result)
        
    def test_drive_valid(self):
        self.vehicle.drive(20)
        result = self.vehicle.fuel
        expected_result = 8.5
        self.assertEqual(result, expected_result)
        
    def test_drive_invalid(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(200)
        self.assertEqual("Not enough fuel", str(context.exception))
        
    def test_refuel_valid(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(5)
        result = self.vehicle.fuel
        expected_result = 26.0
        self.assertEqual(result, expected_result)
        
    def test_refuel_invalid(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(5)
        self.assertEqual("Too much fuel", str(context.exception))
    
    def test_str(self):
        result = str(self.vehicle)
        expected_result = "The vehicle has 150.6 horse power with 33.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected_result)
        

if __name__ == "__main__":
    unittest.main()