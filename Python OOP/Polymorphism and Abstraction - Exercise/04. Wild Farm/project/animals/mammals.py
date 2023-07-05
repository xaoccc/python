from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit, Seed


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"
    
    @property
    def food_to_eat(self):
        return [Vegetable, Fruit]
        
    @property
    def gain_weight(self):
        return 0.10
        
    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
        
class Dog(Mammal):
    def make_sound(self):
        return "Woof!"
    
    @property
    def food_to_eat(self):
        return [Meat]
        
    @property
    def gain_weight(self):
        return 0.40
        
    def  __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
        
class Cat(Mammal):
    def make_sound(self):
        return "Meaow"
        
    @property
    def food_to_eat(self):
        return [Vegetable, Meat]
        
    @property
    def gain_weight(self):
        return 0.30    
        
    def  __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
        
class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"
        
    @property
    def food_to_eat(self):
        return [Meat]
        
    @property
    def gain_weight(self):
        return 1.00    
        
    def  __repr__(self):
        return f"{__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"