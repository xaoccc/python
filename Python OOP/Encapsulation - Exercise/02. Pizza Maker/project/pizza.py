from project.topping import Topping
from project.dough import Dough


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}
    
    @property
    def name(self):
        return self.__name
    
    @property
    def dough(self):
        return self.__dough
        
    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings
        
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value
            
    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value
        
    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value
        
    def add_topping(self, topping: Topping):
        if self.__max_number_of_toppings <= len(self.toppings):
            raise ValueError("Not enough space for another topping")
            
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight
        
    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())

