import unittest


class IntegerList:
    def __init__(self, *args):
        self.integers = []
        for x in args:
            if isinstance(x, int):
                self.integers.append(x)
        
    def add(self, num):
        if not isinstance(num, int):
            raise ValueError("Element is not Integer")
        self.integers.append(num)
        return self.integers

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
            if not isinstance(num, int):
                raise ValueError("Element is not Integer")  
            raise IndexError()
            
    def get_biggest(self):
        return max(self.integers)
        
    def get_index(self, num):
        try:
            return self.integers.index(num)
        except:
            raise IndexError()


        

class ListTests(unittest.TestCase):
    def setUp(self):
        self.my_list = IntegerList(1,2,3)
        
    def test_constructor(self):
        result = self.my_list.integers
        expected_result = [1,2,3]
        self.assertEqual(result, expected_result)
        
        
if __name__ == "__main__":
    unittest.main()
