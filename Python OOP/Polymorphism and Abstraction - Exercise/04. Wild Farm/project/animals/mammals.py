from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def food_to_eat(self):
        return [Vegetable, Fruit]

    def gain_weight(self):
        return 0.10


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def food_to_eat(self):
        return [Meat]

    def gain_weight(self):
        return 0.40


class Cat(Mammal):
    def make_sound(self):
        return "Meaow"

    def food_to_eat(self):
        return [Vegetable, Meat]

    def gain_weight(self):
        return 0.30


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def food_to_eat(self):
        return [Meat]

    def gain_weight(self):
        return 1.00    
        
