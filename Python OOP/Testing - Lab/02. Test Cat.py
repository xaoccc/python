import unittest


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0
        
    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1
        
    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False
        

class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Frodo")
    
    def test_cat_size(self):
        self.cat.eat()
        result = self.cat.size
        expected_result = 1
        self.assertEqual(result, expected_result)
        
    def test_is_fed(self):
        self.cat.eat()
        result = self.cat.fed
        expected_result = True
        self.assertEqual(result, expected_result)
        
    def test_eat_twice(self):
        self.cat.eat()
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual(str(context.exception), 'Already fed.')
        
        
    def test_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual(str(context.exception), 'Cannot sleep while hungry')
        
    def test_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        result = self.cat.sleepy
        expected_result = False
        self.assertEqual(result, expected_result)
        
        
if __name__ == "__main__":
    unittest.main()
