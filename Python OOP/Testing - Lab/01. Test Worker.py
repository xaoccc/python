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
        self.worker = Worker("Pesho", 1000, 50)
        
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
        expected_result = 50
        self.assertEqual(result, expected_result)
        
    def test_rest(self):
        self.worker.rest()
        result = self.worker.energy
        expected_result = 51
        self.assertEqual(result, expected_result)

    
    
if __name__ == '__main__':
    unittest.main()
