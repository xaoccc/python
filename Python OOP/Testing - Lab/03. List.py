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
            raise IndexError("Index is out of range")
            
    def get(self, idx):
        try:
            return self.integers[idx]
        except:
            raise IndexError("Index is out of range")
            
    def insert(self, idx, num):
        if idx < 0 or idx > len(self.integers):
            raise IndexError("Index is out of range")
            
        if not isinstance(num, int):
                raise ValueError("Element is not Integer")
                
        self.integers.insert(idx, num)

             
            
            
    def get_biggest(self):
        return max(self.integers)
        
    def get_index(self, num):
        return self.integers.index(num)



        

class ListTests(unittest.TestCase):
    def setUp(self):
        self.my_list = IntegerList(1,2,"3",3)
        
    def test_constructor(self):
        result = self.my_list.integers
        expected_result = [1,2,3]
        self.assertEqual(result, expected_result)
        
    def test_add_valid(self):
        self.my_list.add(7)
        result = self.my_list.integers
        expected_result = [1,2,3,7]
        self.assertEqual(result, expected_result)
        
    def test_add_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.my_list.add("7")
        self.assertEqual("Element is not Integer", str(context.exception))
        
    def test_remove_valid_index(self):
        self.my_list.remove_index(1)
        result = self.my_list.integers
        expected_result = [1,3]
        self.assertEqual(result, expected_result)
        
    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.remove_index(10)
        self.assertEqual("Index is out of range", str(context.exception))
        
    def test_get_valid_index(self):
        self.my_list.get(2)
        result = self.my_list.integers[2]
        expected_result = 3
        self.assertEqual(result, expected_result)
        
    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.get(20)
        self.assertEqual("Index is out of range", str(context.exception))
        
    def test_insert_valid_type_valid_index(self):
        self.my_list.insert(3, 6)
        result = self.my_list.integers
        expected_result = [1,2,3,6]
        self.assertEqual(result, expected_result)
        
    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.insert(4, 6)
        self.assertEqual("Index is out of range", str(context.exception))
        
    def test_insert_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            self.my_list.insert(3, "6")
        self.assertEqual("Element is not Integer", str(context.exception))
        
    def test_get_biggest(self):
        result = self.my_list.get_biggest()
        expected_result = 3
        self.assertEqual(result, expected_result)
        
    def test_get_index_valid_index(self):
        result = self.my_list.get_index(3)
        expected_result = 2
        self.assertEqual(result, expected_result)
        

        
        
if __name__ == "__main__":
    unittest.main()
