from project.pet_shop import PetShop
import unittest

class TestPetShop(unittest.TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("Petshop")

    def test_init(self):
        self.assertEqual(self.shop.name, "Petshop")
        self.assertEqual(self.shop.food, {})
        self.assertEqual(self.shop.pets, [])

    def test_add_food_negative_error(self):
        with self.assertRaises(ValueError) as valer:
            self.shop.add_food("food", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(valer.exception))

    def test_add_food_zero_error(self):
        with self.assertRaises(ValueError) as valer:
            self.shop.add_food("food", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(valer.exception))

    def test_add_food(self):
        self.assertEqual("Successfully added 20.00 grams of food.", self.shop.add_food("food", 20))
        self.assertEqual({"food": 20}, self.shop.food)
        self.assertEqual("Successfully added 44.00 grams of food.", self.shop.add_food("food", 44))
        self.assertEqual({"food": 64}, self.shop.food)
        self.assertEqual("Successfully added 52.00 grams of more_food.", self.shop.add_food("more_food", 52))
        self.assertEqual({"food": 64, "more_food": 52}, self.shop.food)

    def test_add_pet(self):
        self.assertEqual("Successfully added Archi.", self.shop.add_pet("Archi"))
        self.assertEqual(["Archi"], self.shop.pets)
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Archi")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_no_pet(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("food", "Archi")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet(self):
        self.shop.pets = ["Archi"]
        self.assertEqual('You do not have food', self.shop.feed_pet("food", "Archi"))
        self.assertEqual({}, self.shop.food)
        self.shop.food = {"food": 64, "more_food": 52}
        self.assertEqual("Adding food...", self.shop.feed_pet("food", "Archi"))
        self.assertEqual({"food": 1064, "more_food": 52}, self.shop.food)
        self.assertEqual("Archi was successfully fed", self.shop.feed_pet("food", "Archi"))
        self.assertEqual({"food": 964, "more_food": 52}, self.shop.food)

    def test__repr__(self):
        self.shop.pets = ["Archi", "Frodo"]
        self.assertEqual("Shop Petshop:\nPets: Archi, Frodo", str(self.shop))


if __name__ == "__main__":
    unittest.main()
