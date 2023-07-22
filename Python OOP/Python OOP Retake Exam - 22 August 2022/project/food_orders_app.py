from project.client import Client
from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert

class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients = []

    def register_client(self, client_phone_number: str):
        for client in self.clients:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        self.clients.append(Client(client_phone_number))

    def add_meals_to_menu(self, *meals: Meal):
        acceptable_meals = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
        for meal in meals:
            if meal.__class__.__name__ not in acceptable_meals:
                continue
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
        for client in self.clients:
            if client.phone_number == client_phone_number:
                current_client = client
                break
        if not current_client:
            current_client = Client(client_phone_number)
            self.clients.append(current_client)

        available_meals = []
        for meal in self.menu:
            available_meals.append(meal.name)

        ordered_meals_names = []
        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in available_meals:
                #to-do: remove just the current bill/meals
                current_client.shopping_cart =[]
                current_client.bill = 0.0
                raise Exception(f"{meal_name} is not on the menu!")

            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity < quantity:
                        # to-do: remove just the current bill/meals
                        current_client.shopping_cart = []
                        current_client.bill = 0.0
                        raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
                    current_client.shopping_cart.append(meal)
                    current_client.bill += quantity * meal.price



