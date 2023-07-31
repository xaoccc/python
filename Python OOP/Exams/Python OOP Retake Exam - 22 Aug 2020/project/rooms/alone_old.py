from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name, pension):
        super().__init__(family_name, budget=pension, members_count=1)
        self.room_cost = 10
