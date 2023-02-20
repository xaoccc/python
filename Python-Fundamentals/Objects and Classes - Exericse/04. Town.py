class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"
        
    def set_latitude(self, latitude: str):
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        self.longitude = longitude
        
    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

#test data        
name = input()        
town = Town(name)
latitude_data = input() 
longitude_data = input() 
town.set_latitude(latitude_data)
town.set_longitude(longitude_data)
print(town)     
