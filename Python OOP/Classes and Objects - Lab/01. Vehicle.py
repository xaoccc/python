class Vehicle:
    #mileage - normal attribute
    #max_speed - optional attribute
    #gadgets - instance attribute
    def __init__(self, mileage, max_speed = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []
