from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name, capacity=25):
        super().__init__(name, capacity)