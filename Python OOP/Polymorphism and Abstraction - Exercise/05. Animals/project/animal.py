from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass
