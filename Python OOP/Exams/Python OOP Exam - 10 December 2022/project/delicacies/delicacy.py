from abc import ABC, abstractmethod


class Delicacy(ABC):
    def __init__(self, name: str, price: float, portion: int):
        self.name = name
        self.price = price
        self.portion = portion
        
    @property    
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be null or whitespace!")
        self.__name = value
        
    @property    
    def price(self):
        return self.__price
        
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be less or equal to zero!")
        self.__price = value

    @abstractmethod    
    def details(self):
        pass