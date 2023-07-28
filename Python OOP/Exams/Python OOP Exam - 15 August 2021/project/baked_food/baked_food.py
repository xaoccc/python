from abc import ABC,abstractmethod


class BakedFood(ABC):
    def __init__(self, name, price, portion):
        self.name = name
        self.price = price
        self.portion = portion

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")
        self.__price = value

    @abstractmethod
    def __repr__(self):
        pass
