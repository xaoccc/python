from project.supply.food import Food
from project.supply.drink import Drink
from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    @staticmethod
    def find_player(players, name):
        for player in players:
            if player.name == name:
                return player

    def add_player(self, *args):
        added_players_names = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_players_names.append(player.name)
        return f"Successfully added: {', '.join(added_players_names)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        current_player = self.find_player(self.players, player_name)
        if not current_player or sustenance_type not in ["Food", "Drink"]:
            return
        if not current_player.need_sustenance:
            return f"{player_name} have enough stamina."

        supp = self.supplies[::-1]
        for supply in supp:
            if supply.__class__.__name__ == sustenance_type:
                if supply.energy + current_player.stamina > 100:
                    current_player.stamina = 100
                else:
                    current_player.stamina += supply.energy

                supp.remove(supply)
                self.supplies = supp[::-1]
                return f"{player_name} sustained successfully with {supply.name}."

        if sustenance_type == "Food":
            raise Exception("There are no food supplies left!")

        if sustenance_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.find_player(self.players, first_player_name)
        second_player = self.find_player(self.players, second_player_name)
        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."
        if first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        if second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        if min([first_player.stamina, second_player.stamina]) == first_player.stamina:
            attacker = first_player
            attacked = second_player
        else:
            attacker = second_player
            attacked = first_player

        if attacked.stamina - attacker.stamina / 2 <= 0:
            attacked.stamina = 0
            return f"Winner: {attacker.name}"

        attacked.stamina -= attacker.stamina / 2

        if attacker.stamina - attacked.stamina / 2 <= 0:
            attacker.stamina = 0
            return f"Winner: {attacked.name}"

        attacker.stamina -= attacked.stamina / 2

        if max([first_player.stamina, second_player.stamina]) == first_player.stamina:
            return f"Winner: {first_player.name}"

        return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (2 * player.age) < 0:
                player.stamina = 0
            else:
                player.stamina -= (2 * player.age)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))
        for supply in self.supplies:
            result.append(supply.details())
        return "\n".join(result)

# controller = Controller()
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.add_player(first_player, second_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
#
# print(second_player)
#
# controller.next_day()
#
# print(controller)