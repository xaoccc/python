from project.jockey import Jockey
from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace


class HorseRaceApp:
    horse_breeds = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")
        if horse_type in self.horse_breeds:
            self.horses.append(self.horse_breeds[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."
