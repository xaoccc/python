from project.band_members.drummer import Drummer
from project.band_members.singer import Singer
from project.band_members.guitarist import Guitarist
from project.concert import Concert
from project.band import Band

class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []
        
    def create_musician(self, musician_type: str, name: str, age: int):
        valid_musicians = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
        if musician_type not in valid_musicians:
            raise ValueError("Invalid musician type!")
        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")
        self.musicians.append(valid_musicians[musician_type](name, age))
        return f"{name} is now a {musician_type}."
    
    def create_band(self, name: str):
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."
    
    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."
    
    def add_musician_to_band(self, musician_name: str, band_name: str):
        current_musician, current_band = "", ""
        
        for musician in self.musicians:
            if musician.name == musician_name:
                current_musician = musician
                
        if not current_musician:
            raise Exception(f"{musician_name} isn't a musician!")
            
        for band in self.bands:
            if band.name == band_name:
                current_band = band
        
        if not current_band:
            raise Exception(f"{band_name} isn't a band!")
            
        current_band.members.append(current_musician)
        return f"{musician_name} was added to {band_name}."
    
    def remove_musician_from_band(self, musician_name: str, band_name: str):
        current_musician, current_band = "", ""
            
        for band in self.bands:
            if band.name == band_name:
                current_band = band
                
        if not current_band:
            raise Exception(f"{band_name} isn't a band!")
            
        for musician in current_band.members:
            if musician.name == musician_name:
                current_musician = musician
                
        if not current_musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
            
        current_band.members.remove(current_musician)
        return f"{musician_name} was removed from {band_name}."
    
    def start_concert(self, concert_place: str, band_name: str):
        current_band, current_concert = "", ""
        band_crew = {"Guitarist": 0, "Drummer": 0, "Singer": 0}

        for band in self.bands:
            if band.name == band_name:
                current_band = band
                
        for musician in current_band.members:
            band_crew[musician.__class__.__name__] += 1
        if band_crew["Guitarist"] == 0 or band_crew["Drummer"] == 0 or band_crew["Singer"] == 0:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
            
        for concert in self.concerts:
            if concert.place == concert_place:
                current_concert = concert
                
        genres = {"Rock": ["play the drums with drumsticks", "sing high pitch notes", "play rock"], "Metal": ["play the drums with drumsticks", "sing low pitch notes", "play metal"], "Jazz": ["play the drums with drum brushes", "sing low pitch notes", "sing high pitch notes", "play jazz"]}
        
        for musician in current_band.members: 
            for skill in musician.skills:
                if skill in genres[current_concert.genre]:
                    genres[current_concert.genre].remove(skill)
                    
        if genres[current_concert.genre]:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")           
            
            
        profit =  (current_concert.audience * current_concert.ticket_price) - current_concert.expenses   
        return f"{band_name} gained {profit:.2f}$ from the {current_concert.genre} concert in {concert_place}."
