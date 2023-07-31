from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, budget=pension_two + pension_one, members_count=2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * self.members_count
        self.expenses = sum([item.get_monthly_expense() for item in self.appliances])


