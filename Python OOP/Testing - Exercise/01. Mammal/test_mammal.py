import unittest
from mammal import Mammal
       

class MammalTests(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Frodo", "Cat", "Meow!")
        
    def test_name(self):
        result = self.mammal.name
        expected_result = "Frodo"
        self.assertEqual(result, expected_result)
        
    def test_type(self):
        result = self.mammal.type
        expected_result = "Cat"
        self.assertEqual(result, expected_result)
        
    def test_sound(self):
        result = self.mammal.sound
        expected_result = "Meow!"
        self.assertEqual(result, expected_result)
        
    def test_make_sound(self):
        result = self.mammal.make_sound()
        expected_result = "Frodo makes Meow!"
        self.assertEqual(result, expected_result)
        
    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected_result = "animals"
        self.assertEqual(result, expected_result)
        
    def test_info(self):
        result = self.mammal.info()
        expected_result = "Frodo is of type Cat"
        self.assertEqual(result, expected_result)
        

        
        
if __name__ == "__main__":
    unittest.main()