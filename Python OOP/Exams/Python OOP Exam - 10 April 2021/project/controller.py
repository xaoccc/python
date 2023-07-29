from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.decoration.decoration_repository import DecorationRepository



class Controller:
    def __init__(self):
        self.decorations_repository: DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        pass

    def add_decoration(self, decoration_type: str):
        pass

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        pass

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        pass

    def feed_fish(self, aquarium_name: str):
        pass

    def calculate_value(self, aquarium_name: str):
        pass

    def report(self):
        pass
