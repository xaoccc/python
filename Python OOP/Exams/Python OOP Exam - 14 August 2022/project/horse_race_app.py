from project.jockey import Jockey
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace


class HorseRaceApp:
    horse_breeds = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []


    @staticmethod
    def find_horse(horse_name, horses):
        for horse in horses:
            if horse.name == horse_name:
                return horse
    @staticmethod
    def find_jockey(jockey_name, jockeys):
        for jockey in jockeys:
            if jockey.name == jockey_name:
                return jockey

    @staticmethod
    def find_race(race_type, horse_races):
        for race in horse_races:
            if race.race_type == race_type:
                return race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.find_horse(horse_name, self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.horse_breeds:
            self.horses.append(self.horse_breeds[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_jockey(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.find_race(race_type, self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        current_jockey = self.find_jockey(jockey_name, self.jockeys)
        current_horse = None

        if not current_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        for horse in self.horses:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                current_horse = horse

        if not current_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if current_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        current_jockey.horse = current_horse
        current_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        this_race, this_jockey = self.find_race(race_type, self.horse_races), self.find_jockey(jockey_name, self.jockeys)

        if not this_race:
            raise Exception(f"Race {race_type} could not be found!")

        if not this_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not this_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if this_jockey in this_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        this_race.jockeys.append(this_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        this_race = self.find_race(race_type, self.horse_races)

        if not this_race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(this_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        max_speed, winner_j_name, winner_h_name = 0, "", ""
        for jockey in this_race.jockeys:
            if jockey.horse.speed > max_speed:
                max_speed = jockey.horse.speed
                winner_j_name = jockey.name
                winner_h_name = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {max_speed}km/h is {winner_j_name}! Winner's horse: {winner_h_name}."



# horseRaceApp = HorseRaceApp()
# print(horseRaceApp.add_horse("Appaloosa", "Spirit", 119))
# print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 130))
# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.start_horse_race("Summer"))




