from math import floor

def closest_to_center():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    if ((x1 ** 2) + (y1 ** 2)) / 2 < ((x2 ** 2) + (y2 ** 2)) / 2:
        print(f"({int(floor(x1))}, {int(floor(y1))})")
    else:
        print(f"({int(floor(x2))}, {int(floor(y2))})")
closest_to_center()
