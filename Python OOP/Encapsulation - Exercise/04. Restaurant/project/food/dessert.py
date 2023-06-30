from project.food.food import Food

class Dessert(Food):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self.__calories = calories
    
    @property
    def __calories(self):
        return self.calories
    
    @__calories.setter
    def __calories(self, value):
        self.calories = value
