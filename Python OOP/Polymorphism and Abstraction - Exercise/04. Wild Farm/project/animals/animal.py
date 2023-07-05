from abc import ABC, abstractmethod
from project.food import Vegetable, Meat, Fruit, Seed

class Animal(ABC):
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten
    
    @property
    @abstractmethod
    def food_to_eat(self):
        pass
    
    @property
    @abstractmethod
    def gain_weight(self):
        pass
    
    def feed(self, food):
        if type(food) not in self.food_to_eat:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * self.gain_weight
        self.food_eaten += food.quantity

class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size
        
        
class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region
        
        
