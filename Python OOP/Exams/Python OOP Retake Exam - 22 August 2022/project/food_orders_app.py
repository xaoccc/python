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
            for client_meal in self.menu:
                if client_meal.name == meal.name:
                    meal.quantity += client_meal.quantity


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








