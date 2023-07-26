from project.robot import Robot
import unittest

class RobotTests(unittest.TestCase):        
    def setUp(self):
        self.robot = Robot("007", "Military", 100, 5800)
    
    def test_initialization(self):
        self.assertEqual("007", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(100, self.robot.available_capacity)
        self.assertEqual(5800, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)
        
    def test_invalid_category(self):
        with self.assertRaises(ValueError) as context:
            self.robot.category = "Sex-robot"
        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(context.exception))
        
    def test_invalid_price(self):
        with self.assertRaises(ValueError) as context:
            self.robot.price = -200
        self.assertEqual("Price cannot be negative!", str(context.exception))
        
    def test_upgrade_has_upgrade(self):
        self.robot.upgrade("Machine Gun", 600)
        self.assertEqual("Robot 007 was not upgraded.", self.robot.upgrade("Machine Gun", 600))
        
    def test_upgrade_hardware_upgrades(self):
        self.robot.upgrade("Machine Gun", 600)
        self.assertEqual(['Machine Gun'], self.robot.hardware_upgrades)
        
    def test_upgrade_price(self):
        self.robot.upgrade("Machine Gun", 600)
        self.assertEqual(6700, self.robot.price)
        
    def test_upgrade_print(self):
        self.assertEqual("Robot 007 was upgraded with Machine Gun.", str(self.robot.upgrade("Machine Gun", 600)))
        
    def test_update_no_capacity(self):
        self.assertEqual("Robot 007 was not updated.", self.robot.update(3.11, 200))
        
    def test_update_old_version(self):
        self.robot.update(3.11, 20)
        self.assertEqual("Robot 007 was not updated.", self.robot.update(2.11, 200))
        
    def test_update_updates_list(self):
        self.robot.update(3.11, 20)
        self.robot.update(4.26, 20)
        self.assertEqual([3.11, 4.26], self.robot.software_updates)
        
    def test_update_capacity_decrease(self):
        self.robot.update(3.11, 20)
        self.robot.update(4.26, 45)
        self.assertEqual(35, self.robot.available_capacity)
        
    def test_update_print(self):
        self.assertEqual("Robot 007 was updated to version 4.26.", str(self.robot.update(4.26, 45)))




    def test_upgrade_method_hardware_component_not_in_hardware_upgrades(self):
        result = self.robot.upgrade("Machine Gun", 600)

        self.assertEqual(["Machine Gun"], self.robot.hardware_upgrades)
        self.assertEqual(6700, self.robot.price)
        self.assertEqual(f"Robot 007 was upgraded with Machine Gun.", result)




    def test_gt_method_price_greater_than_other_price(self):
        other = Robot("006", "Military", 100, 4800)

        result = self.robot.__gt__(other)

        self.assertEqual(f"Robot with ID 007 is more expensive than Robot with ID 006.", result)

    def test_gt_method_price_equal_to_other_price(self):
        other = Robot("006", "Military", 100, 5800)

        result = self.robot.__gt__(other)

        self.assertEqual(f"Robot with ID 007 costs equal to Robot with ID 006.", result)

    def test_gt_method_price_less_than_other_price(self):
        other = Robot("006", "Military", 100, 6800)

        result = self.robot.__gt__(other)

        self.assertEqual(f"Robot with ID 007 is cheaper than Robot with ID 006.", result)



if __name__ == "__main__":
    unittest.main()
