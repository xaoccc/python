from project.client import Client
from project.meals.meal import Meal

class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients = []

    def register_client(self, client_phone_number: str):
        for client in self.clients:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        self.clients.append(Client(client_phone_number))