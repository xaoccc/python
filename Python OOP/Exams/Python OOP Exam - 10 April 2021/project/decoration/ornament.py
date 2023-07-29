from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    def __init__(self, comfort=1, price=5):
        super().__init__(comfort, price)