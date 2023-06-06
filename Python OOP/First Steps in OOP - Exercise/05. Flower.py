class Flower:
    is_happy = False
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
    
    
    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True
        
    def status(self):
        if self.is_happy == False:
            return f"{self.name} is not happy" 
        else:
            return f"{self.name} is happy"
