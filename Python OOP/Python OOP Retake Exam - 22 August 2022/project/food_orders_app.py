from project.client import Client
from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert

class FoodOrdersApp:
    receipt_id = 0
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        acceptable_meals = ["Starter", "MainDish", "Dessert"]
        for meal in meals:
            if meal.__class__.__name__ in acceptable_meals:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = []
        for meal in self.menu:
            result.append(meal.details())
        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        current_client = ""
        current_client_bill = 0
        current_shopping_cart = []
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client
                break
        if not current_client:
            current_client = Client(client_phone_number)
            self.clients_list.append(current_client)

        available_meals = []
        for meal in self.menu:
            available_meals.append(meal.name)

        ordered_meals_names = []
        for meal_name, quantity in meal_names_and_quantities.items():

            if meal_name not in available_meals:
                raise Exception(f"{meal_name} is not on the menu!")

            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity < quantity:
                        raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
                    current_shopping_cart.append(meal)
                    meal.quantity -= quantity

                    current_client_bill += quantity * meal.price
                    ordered_meals_names.append(meal.name)
        current_client.bill += current_client_bill
        current_client.shopping_cart += current_shopping_cart
        total_ordered_meals_from_client = []

        for meal in current_client.shopping_cart:
            total_ordered_meals_from_client.append(meal.name)
        return f"Client {client_phone_number} successfully ordered {', '.join(total_ordered_meals_from_client)} for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                current_client = client
                break
        if not current_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        # update the quantity of the meals on the menu list after the cancellation
        for meal in current_client.shopping_cart:
            if meal not in self.menu:
                self.menu.append(meal)


        current_client.shopping_cart = []
        current_client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):


        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                if not client.shopping_cart:
                    raise Exception("There are no ordered meals!")
                current_client = client
                break
        bill = current_client.bill
        self.receipt_id += 1
        current_client.bill = 0
        current_client.shopping_cart = []
        return f"Receipt #{self.receipt_id} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."



food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets)
print(food_orders_app.show_menu())
print(food_orders_app.register_client("0999911111"))

food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}





print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
print(food_orders_app.cancel_order("0899999999"))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)




