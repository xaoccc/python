from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount):
        self.oxygen += amount