from project.plantation import Plantation
import unittest


class TestPlantation(unittest.TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(100)

    def test_init(self):
        self.assertEqual(100, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_invalid(self):
        with self.assertRaises(ValueError) as valer:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(valer.exception))

    def test_size_valid_edge_case(self):
        self.plantation.size = 0
        self.assertEqual(0, self.plantation.size)

    def test_hire_worker_already_hired(self):
        self.plantation.workers = ["Pesho"]
        with self.assertRaises(ValueError) as valer:
            self.plantation.hire_worker("Pesho")
        self.assertEqual("Worker already hired!", str(valer.exception))

    def test_hire_worker(self):
        self.assertEqual("Pesho successfully hired.", self.plantation.hire_worker("Pesho"))
        self.assertEqual(["Pesho"], self.plantation.workers)
        self.assertEqual("Vankata successfully hired.", self.plantation.hire_worker("Vankata"))
        self.assertEqual(["Pesho", "Vankata"], self.plantation.workers)

    def test__len__(self):
        self.plantation.plants = {"Pesho": ["Rose"], "Vankata": ["Carrot", "Tomato"]}
        self.assertEqual(3, self.plantation.__len__())

    def test_planting_no_worker(self):
        self.plantation.workers = ["Pesho"]
        with self.assertRaises(ValueError) as valer:
            self.plantation.planting("Vankata", "Lily")
        self.assertEqual("Worker with name Vankata is not hired!", str(valer.exception))

    def test_planting_no_place_size_equal_to_len(self):
        self.plantation.workers = ["Pesho", "Vankata"]
        self.plantation.plants = {"Pesho": ["Rose"], "Vankata": ["Carrot", "Tomato"]}
        self.plantation.size = 3
        with self.assertRaises(ValueError) as valer:
            self.plantation.planting("Pesho", "Lily")
        self.assertEqual("The plantation is full!", str(valer.exception))

    def test_planting_no_place_size_less_than_len(self):
        self.plantation.workers = ["Pesho", "Vankata"]
        self.plantation.plants = {"Pesho": ["Rose"], "Vankata": ["Carrot", "Tomato"]}
        self.plantation.size = 2
        with self.assertRaises(ValueError) as valer:
            self.plantation.planting("Pesho", "Lily")
        self.assertEqual("The plantation is full!", str(valer.exception))

    def test_planting_not_first_plant(self):
        self.plantation.workers = ["Pesho", "Vankata"]
        self.plantation.plants = {"Pesho": ["Rose"], "Vankata": ["Carrot", "Tomato"]}
        self.assertEqual(f"Pesho planted Lily.", self.plantation.planting("Pesho", "Lily"))
        self.assertEqual({"Pesho": ["Rose", "Lily"], "Vankata": ["Carrot", "Tomato"]}, self.plantation.plants)

    def test_planting_first_plant(self):
        self.plantation.workers = ["Pesho", "Vankata"]
        self.plantation.plants = {"Vankata": ["Carrot", "Tomato"]}
        self.assertEqual(f"Pesho planted it's first Lily.", self.plantation.planting("Pesho", "Lily"))
        self.assertEqual({"Pesho": ["Lily"], "Vankata": ["Carrot", "Tomato"]}, self.plantation.plants)

    def test__str__with_data(self):
        self.plantation.workers = ["Pesho", "Vankata"]
        self.plantation.plants = {"Pesho": ["Rose"], "Vankata": ["Carrot", "Tomato"]}
        self.assertEqual("Plantation size: 100\nPesho, Vankata\n"
                         "Pesho planted: Rose\n"
                         "Vankata planted: Carrot, Tomato", str(self.plantation))

    def test__str__no_data(self):
        self.assertEqual("Plantation size: 100\n", str(self.plantation))

    def test__repr__with_data(self):
        self.plantation.workers = ["Pesho", "Vankata"]
        self.plantation.plants = {"Pesho": ["Rose"], "Vankata": ["Carrot", "Tomato"]}
        self.assertEqual("Size: 100\nWorkers: Pesho, Vankata", self.plantation.__repr__())

    def test__repr__no_data(self):
        self.assertEqual("Size: 100\nWorkers: ", self.plantation.__repr__())


if __name__ == "__main__":
    unittest.main()
