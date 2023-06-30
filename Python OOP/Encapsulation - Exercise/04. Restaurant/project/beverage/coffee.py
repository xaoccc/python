from project.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50
    
    def __init__(self, name, caffeine):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine
    
    @property
    def __caffeine(self):
        return self.caffeine
    
    @__caffeine.setter
    def __caffeine(self, value):
        self.caffeine = value