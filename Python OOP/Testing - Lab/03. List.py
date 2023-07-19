import unittest


class IntegerList:
    def __init__(self):
        self.integers = []
        
    def add(self, num):
        try:
            self.integers.append(num)
            return self.integers
        except:
            raise ValueError()
            
    def remove_index(self, idx):
        try:
            self.integers.pop(idx)
        except:
            raise IndexError()
            
    def get(self, idx):
        try:
            return self.integers[idx]
        except:
            raise IndexError()
            
    def insert(self, idx, num):
        try: 
            self.integers.insert(idx, num)
        except:
            raise ValueError() if not isinstance(num, int) else raise IndexError()
            
    def get_biggest(self):
        return max(self.integers)
        
    def get_index(self, num):
        try:
            return self.integers.index(num)
        except:
            raise IndexError()


        

class CatTests(unittest.TestCase):
    def setUp(self):
        
        
if __name__ == "__main__":
    unittest.main()
