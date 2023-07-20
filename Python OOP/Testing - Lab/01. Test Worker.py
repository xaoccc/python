import unittest

class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0
        
    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1
            
    def rest(self):
        self.energy += 1
        
    def get_info(self):
        return f'{self.name} has saved {self.money} money.'
        
        
class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Pesho", 1000, 0)
        
    def test_worker_name(self):    
        result = self.worker.name
        expected_result = "Pesho"
        self.assertEqual(result, expected_result)
        
    def test_worker_salary(self):    
        result = self.worker.salary
        expected_result = 1000
        self.assertEqual(result, expected_result)
        
    def test_worker_energy(self):    
        result = self.worker.energy
        expected_result = 0
        self.assertEqual(result, expected_result)
        
    def test_rest(self):
        self.worker.rest()
        result = self.worker.energy
        expected_result = 1
        self.assertEqual(result, expected_result)
        
    def test_negative_or_zero_energy(self):
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')
        self.assertEqual(self.worker.money, 0)  # Money should not be earned
        self.assertEqual(self.worker.energy, 0)  # Energy should remain 0
    
    def test_money_earned(self):
        self.worker = Worker("Pesho", 1000, 50)
        self.worker.work()
        result = self.worker.money
        expected_result = 1000
        self.assertEqual(result, expected_result)
        
    def test_energy_decreased(self):
        self.worker = Worker("Pesho", 1000, 50)
        self.worker.work()
        result = self.worker.energy
        expected_result = 49
        self.assertEqual(result, expected_result)
        
    def test_get_info(self):
        result = self.worker.get_info()
        expected_result = "Pesho has saved 0 money."
        self.assertEqual(result, expected_result)
    
    
if __name__ == '__main__':
    unittest.main()
