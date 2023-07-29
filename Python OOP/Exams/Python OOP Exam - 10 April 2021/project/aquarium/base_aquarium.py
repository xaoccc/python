from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def calculate_comfort(self):
        return sum([decoration.comfort for decoration in self.decorations])

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."

        if fish.__class__.__name__[:7] != self.__class__.__name__[:7]:
            return "Water not suitable."

        if fish.__class__.__name__ in ["FreshwaterFish", "SaltwaterFish"]:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        if self.fish:
            return f"{self.name}:\nFish: {' '.join([fish.name for fish in self.fish])}\nDecorations: {len(self.decorations)}\nComfort: {sum([dec.comfort for dec in self.decorations])}"
        return f"{self.name}:\nFish: none\nDecorations: {len(self.decorations)}\nComfort: {sum([dec.comfort for dec in self.decorations])}"

