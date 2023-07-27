from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.meteorologist import Meteorologist
from project.astronaut.geodesist import Geodesist
from project.planet.planet import Planet


class SpaceStation:
    astronaut_types = {"Biologist": Biologist, "Meteorologist": Meteorologist, "Geodesist": Geodesist}
    successful_missions, failed_missions = 0, 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.astronaut_types:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        self.astronaut_repository.add(self.astronaut_types[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        self.planet_repository.add(Planet(name))
        self.planet_repository.planets[-1].items += items.split(", ")
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")

        suitable_astronauts = []
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                suitable_astronauts.append(astronaut)
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        planet = self.planet_repository.find_by_name(planet_name)

        suitable_astronauts = sorted(suitable_astronauts, key=lambda a: -a.oxygen)[:5]
        participating_astronauts = []
        for astronaut in suitable_astronauts:
            while astronaut.oxygen > 0:
                if astronaut.name not in participating_astronauts:
                    participating_astronauts.append(astronaut.name)

                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

                if not planet.items:
                    self.successful_missions += 1
                    return f"Planet: {planet_name} was explored. {len(participating_astronauts)} astronauts participated in collecting items."

        if planet.items:
            self.failed_missions += 1
            return "Mission is not completed."

    def report(self):
        result = [f"{self.successful_missions} successful missions!\n"
                  f"{self.failed_missions} missions were not completed!\nAstronauts' info:"]
        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}\nOxygen: {astronaut.oxygen}")
            if astronaut.backpack:
                result.append(f"Backpack items: {', '.join(astronaut.backpack)}")
            else:
                result.append(f"Backpack items: none")

        return str("\n".join(result))


