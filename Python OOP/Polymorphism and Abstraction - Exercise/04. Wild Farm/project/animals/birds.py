from project.animals.animal import Bird
from project.food import Vegetable, Meat, Fruit, Seed
        
        
class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"
        
    @property
    def food_to_eat(self):
        return [Meat]
        
    @property
    def gain_weight(self):
        return 0.25
        
    def  __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
        
        
class Hen(Bird):
    def make_sound(self):
        return "Cluck"
        
    @property
    def food_to_eat(self):
        return [Vegetable, Meat, Fruit, Seed]
        
    @property
    def gain_weight(self):
        return 0.35
        
    def  __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"