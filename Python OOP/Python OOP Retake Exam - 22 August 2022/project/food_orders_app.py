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

