from project.meals.starter import Starter
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert
from project.client import Client


class FoodOrdersApp:
    receipt_id = 0
    valid_meals = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
    def __init__(self):
        self.menu = []
        self.clients_list = []

    @staticmethod
    def find_client(phone_number, clients):
        for client in clients:
            if client.phone_number == phone_number:
                return client

    @staticmethod
    def find_meal(meal_name, menu):
        for meal in menu:
            if meal.name == meal_name:
                return meal

    def register_client(self, client_phone_number: str):
        client = self.find_client(client_phone_number, self.clients_list)
        if not client:
            self.clients_list.append(Client(client_phone_number))
            return f"Client {client_phone_number} registered successfully."

        raise Exception("The client has already been registered!")

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in self.valid_meals:
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
        client = self.find_client(client_phone_number, self.clients_list)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for meal_name in meal_names_and_quantities.keys():
            if not self.find_meal(meal_name, self.menu):
                raise Exception(f"{meal_name} is not on the menu!")

        for meal_name, meal_qty  in meal_names_and_quantities.items():
            current_meal = self.find_meal(meal_name, self.menu)
            if current_meal.quantity < meal_qty:
                raise Exception(f"Not enough quantity of {current_meal.__class__.__name__}: {meal_name}!")

        for meal_name, meal_qty in meal_names_and_quantities.items():
            current_meal = self.find_meal(meal_name, self.menu)
            if current_meal.__class__.__name__ in self.valid_meals:
                current_meal.quantity -= meal_qty
                client.shopping_cart.append(self.valid_meals[current_meal.__class__.__name__](meal_name, current_meal.price, meal_qty))

                client.bill += current_meal.price * meal_qty
        return f"Client {client_phone_number} successfully ordered {', '.join([meal.name for meal in client.shopping_cart])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.find_client(client_phone_number, self.clients_list)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in self.menu:
            for client_meal in client.shopping_cart:
                if meal.name == client_meal.name:
                    meal.quantity += client_meal.quantity

        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.find_client(client_phone_number, self.clients_list)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        total_paid_money = client.bill
        client.bill = 0
        client.shopping_cart = []

        self.receipt_id += 1
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."








