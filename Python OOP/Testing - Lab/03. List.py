import unittest

class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)
        

class ListTests(unittest.TestCase):
    def setUp(self):
        self.my_list = IntegerList(1,2,"3",3)
        
    def test_constructor(self):
        result = self.my_list.get_data()
        expected_result = [1,2,3]
        self.assertEqual(result, expected_result)
        
    def test_add_valid(self):
        self.my_list.add(7)
        result = self.my_list.get_data()
        expected_result = [1,2,3,7]
        self.assertEqual(result, expected_result)
        
    def test_add_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.my_list.add("7")
        self.assertEqual("Element is not Integer", str(context.exception))
        
    def test_remove_valid_index(self):
        self.my_list.remove_index(1)
        result = self.my_list.get_data()
        expected_result = [1,3]
        self.assertEqual(result, expected_result)
        
    def test_remove_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.remove_index(10)
        self.assertEqual("Index is out of range", str(context.exception))
        
    def test_get_valid_index(self):
        self.my_list.get(2)
        result = self.my_list.get_data()[2]
        expected_result = 3
        self.assertEqual(result, expected_result)
        
    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.get(20)
        self.assertEqual("Index is out of range", str(context.exception))
        
    def test_insert_valid_type_valid_index(self):
        self.my_list.insert(2, 6)
        result = self.my_list.get_data()
        expected_result = [1,2,6,3]
        self.assertEqual(result, expected_result)
        
    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.my_list.insert(4, 6)
        self.assertEqual("Index is out of range", str(context.exception))
        
    def test_insert_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            self.my_list.insert(2, "6")
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
