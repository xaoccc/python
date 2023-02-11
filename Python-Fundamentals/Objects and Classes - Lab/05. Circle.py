class Circle:
    #This is a local variable for the class
    __pi = 3.14
    #Here we must have at least 1 attribute - self. The other attribute takes a value like this CLASSNAME(VALUE) and append it to some variable as below
    def __init__(self, diameter):
        #We define 2 variables we can use in the methods by writing "self" as an attribute
        self.diameter = diameter
        self.radius = diameter / 2
        
    def calculate_circumference(self):
        #In the class method we access the local variable by writing CLASSNAME.LOCAL_VARIABLE_NAME
        #self.diameter == diameter == 10
        return Circle.__pi * self.diameter
        
    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius
        
    def calculate_area_of_sector(self, angle):
        return (angle / 360) * Circle.__pi * self.radius * self.radius
    
#Testing area(not included in submit). It is out of the class:
#1. We have a variable which has 2 purposes - 1. to give the class attibute a value 2. To be used in the output as the class function here is a custom method for the variable
circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")

