from project.meals.meal import Meal


class Starter(Meal):
    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"