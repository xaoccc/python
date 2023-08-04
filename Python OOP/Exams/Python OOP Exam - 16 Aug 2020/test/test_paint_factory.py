from project.factory.paint_factory import PaintFactory
import unittest


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Giga Paint", 100)

    def test_init(self):
        self.assertEqual("Giga Paint", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual({}, self.factory.products)

    def test_add_ingredients_invalid_ingredient(self):
        self.assertEqual({}, self.factory.products)
        with self.assertRaises(TypeError) as te:
            self.factory.add_ingredient("pink", 20)
        self.assertEqual("Ingredient of type pink not allowed in PaintFactory", str(te.exception))
        self.assertEqual({}, self.factory.products)

    def test_add_ingredients_no_space(self):
        self.factory.ingredients = {"blue": 30, "red": 60}
        self.assertEqual({"blue": 30, "red": 60}, self.factory.products)
        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient("yellow", 11)
        self.assertEqual("Not enough space in factory", str(ve.exception))
        self.assertEqual({"blue": 30, "red": 60}, self.factory.products)

    def test_add_ingredients(self):
        self.assertEqual({}, self.factory.products)
        self.factory.add_ingredient("blue", 30)
        self.assertEqual({"blue": 30}, self.factory.products)
        self.factory.add_ingredient("red", 60)
        self.assertEqual({"blue": 30, "red": 60}, self.factory.products)
        self.factory.add_ingredient("yellow", 8)
        self.assertEqual({"blue": 30, "red": 60, "yellow": 8}, self.factory.products)
        self.factory.add_ingredient("yellow", 2)
        self.assertEqual({"blue": 30, "red": 60, "yellow": 10}, self.factory.products)

    def test_remove_ingredient_no_such_ingredient(self):
        self.assertEqual({}, self.factory.products)
        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient("red", 31)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))
        self.assertEqual({}, self.factory.products)
        self.factory.ingredients = {"blue": 30, "red": 60}
        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient("yellow", 31)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_negative_quantity(self):
        self.factory.ingredients = {"blue": 30, "red": 60}
        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient("red", 61)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))
        self.factory.ingredients = {"blue": 30, "red": 60}

    def test_remove_ingredient(self):
        self.factory.ingredients = {"blue": 30, "red": 60}
        self.factory.remove_ingredient("red", 20)
        self.factory.ingredients = {"blue": 30, "red": 40}
        self.factory.remove_ingredient("red", 40)
        self.factory.ingredients = {"blue": 30, "red": 0}
        self.factory.remove_ingredient("blue", 30)
        self.factory.ingredients = {"blue": 0, "red": 0}

if __name__ == "__main__":
    unittest.main()
