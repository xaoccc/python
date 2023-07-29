from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.decoration.decoration_repository import DecorationRepository



class Controller:
    aq_types = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}
    fish_types = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}
    decor_types = {"Ornament": Ornament, "Plant": Plant}
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []


    @staticmethod
    def find_aquarium(aquarium_name, aquariums):
        for aquarium in aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

    @staticmethod
    def find_decoration(decoration_type, decorations):
        for decoration in decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.aq_types:
            return "Invalid aquarium type."

        self.aquariums.append(self.aq_types[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.decor_types:
            return "Invalid decoration type."
        self.decorations_repository.decorations.append(self.decor_types[decoration_type]())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.find_aquarium(aquarium_name, self.aquariums)
        decoration = self.find_decoration(decoration_type, self.decorations_repository.decorations)
        if not decoration or not aquarium:
            return f"There isn't a decoration of type {decoration_type}."


        self.decorations_repository.decorations.remove(decoration)
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.fish_types:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.find_aquarium(aquarium_name, self.aquariums)
        return aquarium.add_fish(self.fish_types[fish_type](fish_name, fish_species, price))

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name, self.aquariums)
        for fish in aquarium.fish:
            fish.eat()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name, self.aquariums)
        total = 0

        for fish in aquarium.fish:
            total += fish.price

        for decoration in aquarium.decorations:
            total += decoration.price

        return f"The value of Aquarium {aquarium_name} is {total:.2f}."


    def report(self):
        result = []
        for aqua in self.aquariums:
            result.append(str(aqua))
            result.append(f"Decorations: {len(aqua.decorations)}")
            result.append(f"Comfort: {sum([dec.comfort for dec in aqua.decorations])}")

        return "\n".join(result)


