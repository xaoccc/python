from project.shopping_cart import ShoppingCart
import unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Shop", 500)


    def test_init(self):
        self.assertEqual("Shop", self.cart.shop_name)
        self.assertEqual(500, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_invalid_shop_name_nums(self):
        with self.assertRaises(Exception) as ex:
            self.cart.shop_name = "123"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_invalid_shop_first_letter_lowercase(self):
        with self.assertRaises(Exception) as ex:
            self.cart.shop_name = "aaa"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_add_to_cart_too_expensive_product(self):
        with self.assertRaises(ValueError) as valer:
            self.cart.add_to_cart("Vodka", 101)
        self.assertEqual(f"Product Vodka cost too much!", str(valer.exception))

    def test_add_to_cart_valid_price(self):
        self.assertEqual("Vodka product was successfully added to the cart!", self.cart.add_to_cart("Vodka", 15))
        self.assertEqual({"Vodka": 15}, self.cart.products)

    def test_remove_from_cart_error(self):
        with self.assertRaises(ValueError) as valer:
            self.cart.remove_from_cart("Vodka")
        self.assertEqual("No product with name Vodka in the cart!", str(valer.exception))

    def test_remove_from_cart_valid_product(self):
        self.cart.add_to_cart("Vodka", 15)
        self.assertEqual("Product Vodka was successfully removed from the cart!", self.cart.remove_from_cart("Vodka"))
        self.assertEqual({}, self.cart.products)

    def test__add__method(self):
        shop = ShoppingCart("Shop", 500)
        shop.add_to_cart('Vodka', 10)
        other = ShoppingCart("OtherShop", 1000)
        other.add_to_cart("Rakia", 20)
        new_cart = shop.__add__(other)
        self.assertEqual("ShopOtherShop", new_cart.shop_name)
        self.assertEqual(1500, new_cart.budget)
        self.assertEqual({"Vodka": 10, "Rakia": 20}, new_cart.products)

    def test__add__method_then_remove_valid(self):
        shop = ShoppingCart("Shop", 500)
        shop.add_to_cart('Vodka', 10)
        other = ShoppingCart("OtherShop", 1000)
        other.add_to_cart("Rakia", 20)
        new_cart = shop.__add__(other)
        self.assertEqual("Product Vodka was successfully removed from the cart!", new_cart.remove_from_cart("Vodka"))
        self.assertEqual({"Rakia": 20}, new_cart.products)

    def test__add__method_then_remove_invalid(self):
        shop = ShoppingCart("Shop", 500)
        shop.add_to_cart('Vodka', 10)
        other = ShoppingCart("OtherShop", 1000)
        other.add_to_cart("Rakia", 20)
        new_cart = shop.__add__(other)
        with self.assertRaises(ValueError) as valer:
            new_cart.remove_from_cart("Whisky")
        self.assertEqual("No product with name Whisky in the cart!", str(valer.exception))

    def test_buy_products_cost_too_much(self):
        self.cart = ShoppingCart("Shop", 150)
        self.cart.add_to_cart("Vodka", 99)
        self.cart.add_to_cart("Rakia", 66)
        with self.assertRaises(ValueError) as valer:
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 15.00lv!", str(valer.exception))

    def test_buy_products_cost_valid_sum(self):
        self.cart.add_to_cart("Vodka", 99)
        self.assertEqual("Products were successfully bought! Total cost: 99.00lv.", self.cart.buy_products())





if __name__ == "__main__":
    unittest.main()