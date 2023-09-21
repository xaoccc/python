import math
r = 5
a = 20
b = 10
circle_area = math.pi * r ** 2
rect_area = a * b
area_between_circles_and_rect = rect_area - (2 * circle_area)
each_corner_area = area_between_circles_and_rect / 8
triangle_area = r * b / 2
cirle_part_area = (r ** 2) * (math.pi / 2) - (r ** 2) * (math.atan(1/2)) - 10
small_corner_part_area = triangle_area - each_corner_area - cirle_part_area
red_area = rect_area / 2 - circle_area - small_corner_part_area

print(red_area)
