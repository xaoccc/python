from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, name, portion, brand, price):
        self.name = name
        self.portion = portion
        self.brand = brand
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if value.strip() == "":
            raise ValueError("Brand cannot be empty string or white space!")
        self.__brand = value


    @abstractmethod
    def __repr__(self):
        pass