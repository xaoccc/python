eggs_num = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_num = 0
for i in range(eggs_num):
    egg_color = input()
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1
if red_eggs > max_num:
    max_num = red_eggs
    max_num_color = "red"
if orange_eggs > max_num:
    max_num = orange_eggs
    max_num_color = "orange"
if blue_eggs > max_num:
    max_num = blue_eggs
    max_num_color = "blue"
if green_eggs > max_num:
    max_num = green_eggs
    max_num_color = "green"
    
print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_num} -> {max_num_color}")
