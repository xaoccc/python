from project.train.train import Train
import unittest


class TestTrain(unittest.TestCase):
    def setUp(self) -> None:
        self.train = Train("BigTrain", 2)

    def test_init(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)
        self.assertEqual("BigTrain", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_full_train_error(self):
        self.train.passengers = ["Jim", "Bob"]
        with self.assertRaises(ValueError) as valer:
            self.train.add("Jack")
        self.assertEqual("Train is full", str(valer.exception))
        self.assertEqual(["Jim", "Bob"], self.train.passengers)

    def test_add_passenger_exists_error(self):
        self.train.passengers = ["Jim"]
        with self.assertRaises(ValueError) as valer:
            self.train.add("Jim")
        self.assertEqual("Passenger Jim Exists", str(valer.exception))
        self.assertEqual(["Jim"], self.train.passengers)

    def test_add(self):
        self.train.passengers = ["Jim"]
        self.assertEqual("Added passenger Jack", self.train.add("Jack"))
        self.assertEqual(["Jim", "Jack"], self.train.passengers)

    def test_remove_not_found_error(self):
        self.train.passengers = ["Jim", "Bob"]
        with self.assertRaises(ValueError) as valer:
            self.train.remove("Jack")
        self.assertEqual("Passenger Not Found", str(valer.exception))

    def test_remove(self):
        self.train.passengers = ["Jim", "Bob"]
        self.assertEqual("Removed Jim", self.train.remove("Jim"))
        self.assertEqual(["Bob"], self.train.passengers)


if __name__ == "__main__":
    unittest.main()
