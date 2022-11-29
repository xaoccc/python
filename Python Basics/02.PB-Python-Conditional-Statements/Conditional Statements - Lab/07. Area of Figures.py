#user input
figure = input()
area = 0
from math import pi

#logic
if figure == "square":
    side = float(input())
    area = side ** 2
elif figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
elif figure == "circle":
    radius = float(input())
    area = radius ** 2 * pi
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = side * height / 2

#output
print(figure)
print(f"{area:.3f}")