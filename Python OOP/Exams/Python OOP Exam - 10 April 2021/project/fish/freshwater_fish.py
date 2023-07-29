from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    def __init__(self, name, species, price, size=3):
        super().__init__(name, species, price, size)

    def eat(self):
        self.size += 3
