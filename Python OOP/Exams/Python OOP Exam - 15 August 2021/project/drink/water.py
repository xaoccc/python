from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name, portion, brand, price=1.50):
        super().__init__(name, portion, brand, price)

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"