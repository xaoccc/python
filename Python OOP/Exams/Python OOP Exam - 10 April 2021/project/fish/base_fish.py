from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name, species, price, size):
        self.name = name
        self.species = species
        self.price = price
        self.size = size


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        if value.strip() == "":
            raise ValueError("Fish name cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self.__price = value

    @abstractmethod
    def eat(self):
        self.size += 5