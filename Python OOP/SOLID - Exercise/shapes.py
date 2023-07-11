from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def get_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)

    def get_area(self):
        return self.base * self.height

class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.width * shape.height

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
