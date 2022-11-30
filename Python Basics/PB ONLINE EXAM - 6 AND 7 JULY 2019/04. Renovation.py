from math import ceil
h = int(input())
w = int(input())
paint_total = 0
paint_left = 0
total_area = h * w * 4
paintless = int(input())
paint_area = ceil(total_area - ((paintless * total_area) / 100))
while paint_total <= paint_area:
    paint = input()
    if paint == "Tired!":
        print(f"{paint_left} quadratic m left.")
        break
    paint_total += int(paint)
    paint_left = abs(paint_area - paint_total)
    if paint_left == 0: 
        print("All walls are painted! Great job, Pesho!")
        break
else:
    print(f"All walls are painted and you have {paint_left} l paint left!")
