from project.toy_store import ToyStore
import unittest

class TestToyStore(unittest.TestCase):
    def test_init(self):
        toy_store = ToyStore()
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, toy_store.toy_shelf)
    def test_add_toy_empty_shelf(self):
        toy_store = ToyStore()
        result = toy_store.add_toy('A', 'Teddy Bear')
        self.assertEqual(result, 'Toy:Teddy Bear placed successfully!')
        self.assertEqual(toy_store.toy_shelf['A'], 'Teddy Bear')

    def test_remove_toy_from_shelf(self):
        toy_store = ToyStore()
        toy_store.add_toy('A', 'Teddy Bear')
        result = toy_store.remove_toy('A', 'Teddy Bear')
        self.assertEqual(result, 'Remove toy:Teddy Bear successfully!')
        self.assertIsNone(toy_store.toy_shelf['A'])

    def test_add_toy_nonexistent_shelf(self):
        toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            toy_store.add_toy('H', 'Teddy Bear')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_occupied_shelf(self):
        toy_store = ToyStore()
        toy_store.add_toy('A', 'Teddy Bear')
        with self.assertRaises(Exception) as ex:
            toy_store.add_toy('A', 'Barbie Doll')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_already_in_shelf(self):
        toy_store = ToyStore()
        toy_store.add_toy('A', 'Teddy Bear')
        with self.assertRaises(Exception) as ex:
            toy_store.add_toy('A', 'Teddy Bear')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))


    def test_remove_toy_nonexistent_shelf(self):
        toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            toy_store.remove_toy('H', 'Teddy Bear')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_nonexistent_toy_from_shelf(self):
        toy_store = ToyStore()
        with self.assertRaises(Exception) as ex:
            toy_store.remove_toy('A', 'Teddy Bear')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_from_all_shelves(self):
        toy_store = ToyStore()
        for shelf in toy_store.toy_shelf.keys():
            toy_store.add_toy(shelf, 'Teddy Bear')
        for shelf in toy_store.toy_shelf.keys():
            result = toy_store.remove_toy(shelf, 'Teddy Bear')
            self.assertEqual(result, f'Remove toy:Teddy Bear successfully!')
            self.assertIsNone(toy_store.toy_shelf[shelf])

    def test_add_toy_normal(self):
        toy_store = ToyStore()
        toy_store.add_toy('A', "Teddy")
        self.assertEqual("Teddy", toy_store.toy_shelf['A'])




if __name__ == "__main__":
    unittest.main()
