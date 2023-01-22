from math import sqrt

x = 3
y = 1
z = sqrt((x ** 2) + (y ** 2))

a = x * ( y / z )
b = a / 2
c = z - a - b

print(c ** 2)
