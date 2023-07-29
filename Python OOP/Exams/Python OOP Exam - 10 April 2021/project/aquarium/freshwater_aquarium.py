from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name, capacity=50):
        super().__init__(name, capacity)