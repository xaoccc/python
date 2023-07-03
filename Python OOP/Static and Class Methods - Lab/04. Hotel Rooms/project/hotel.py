from project.room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0
        
    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")
        
    def add_room(self, room: Room):
        self.rooms.append(room)
        
    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number and not room.is_taken:
                room.take_room(people)
                self.guests += room.guests
                
    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number and room.is_taken:
                self.guests -= room.guests
                room.free_room()
                
    def status(self):
        free, taken = [], []
        for room in self.rooms:
            if room.is_taken:
                taken.append(room.number)
            else:
                free.append(room.number)
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join([str(i) for i in free])}\nTaken rooms: {', '.join([str(i) for i in taken])}"