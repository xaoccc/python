from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=2 + len(children))
        self.room_cost = 30
        self.children = [child for child in children]
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = sum([item.get_monthly_expense() for item in self.appliances]) + sum([child.get_monthly_expense() for child in self.children])


