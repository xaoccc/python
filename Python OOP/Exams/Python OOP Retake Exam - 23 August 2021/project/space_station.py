class SpaceStation:
    def __init__(self, planet_repository, astronaut_repository):
        self.planet_repository = planet_repository
        self.astronaut_repository = astronaut_repository

    def add_astronaut(self, astronaut_type: str, name: str):
        pass

    def add_planet(self, name: str, items: str):
        pass

    def retire_astronaut(self, name: str):
        pass

    def recharge_oxygen(self):
        pass

    def send_on_mission(self, planet_name: str):
        pass

    def report(self):
        pass
