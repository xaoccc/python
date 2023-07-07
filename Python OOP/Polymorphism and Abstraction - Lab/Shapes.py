import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Trapezoid(Shape):
    def __init__(self, base_side, top_side, height):
        self.base_side = base_side
        self.top_side = top_side
        self.height = height
     
    def calculate_area(self):
        return (self.base_side + self.top_side) * self.height / 2 
        
        
class Octagon(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2 * (1 + math.sqrt(2)) * 2
        
# Usage
rectangle = Rectangle(5, 10)
triangle = Triangle(4, 6)
circle = Circle(3)
trapezoid = Trapezoid(13, 9, 4)
octagon = Octagon(6)

# We can just specify the shape and call the SAME method:
print(rectangle.calculate_area())  # Output: 50
print(triangle.calculate_area())  # Output: 12.0
print(circle.calculate_area())  # Output: 28.274333882308138
print(trapezoid.calculate_area())  # Output: 44.0   
print(octagon.calculate_area())  # Output: 173.82337649086284
