import math

class Shape:
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

# Usage
rectangle = Rectangle(5, 10)
triangle = Triangle(4, 6)
circle = Circle(3)

print(rectangle.calculate_area())  # Output: 50
print(triangle.calculate_area())  # Output: 12.0
print(circle.calculate_area())  # Output: 28.274333882308138
