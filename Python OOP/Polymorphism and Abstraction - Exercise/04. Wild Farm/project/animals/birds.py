from project.animals.animal import Bird
from project.food import Vegetable, Meat, Fruit, Seed
        
        
class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def food_to_eat(self):
        return [Meat]

    def gain_weight(self):
        return 0.25


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def food_to_eat(self):
        return [Vegetable, Meat, Fruit, Seed]

    def gain_weight(self):
        return 0.35
        
