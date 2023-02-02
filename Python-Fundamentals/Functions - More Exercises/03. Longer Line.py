import math
x1, y1, x2, y2, x3, y3, x4, y4 = math.floor(float(input())), math.floor(float(input())), math.floor(float(input())), math.floor(float(input())), math.floor(float(input())), math.floor(float(input())), math.floor(float(input())), math.floor(float(input()))

sum_x = math.floor(abs(x1) + abs(y1))
sum_y = math.floor(abs(x2) + abs(y2))
sum_z = math.floor(abs(x3) + abs(y3))
sum_v = math.floor(abs(x4) + abs(y4))

def longest_line(sum_x, sum_y, sum_z, sum_v):

    line1_length = sum_x + sum_y
    line2_length = sum_z + sum_v
    
    if line1_length > line2_length:
        if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
            return f"({x1}, {y1})({x2}, {y2})"
        else:
            return f"({x2}, {y2})({x1}, {y1})"
    elif line1_length < line2_length:
        if abs(x3) + abs(y3) <= abs(x4) + abs(y4):
            return f"({x3}, {y3})({x4}, {y4})"
        else:
            return f"({x4}, {y4})({x3}, {y3})"
    else:
        if abs(x3) + abs(y3) > abs(x4) + abs(y4):
            return f"({x4}, {y4})({x3}, {y3})"
        else:
            return f"({x3}, {y3})({x4}, {y4})"

print(longest_line(sum_x, sum_y, sum_z, sum_v))

