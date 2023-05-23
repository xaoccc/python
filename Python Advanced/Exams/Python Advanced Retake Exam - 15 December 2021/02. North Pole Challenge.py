workshop = [] 
rows, cols  = [int(i) for i in input().split(", ")]
decoration_collected, gifts_collected, cookies_collected = 0, 0, 0
decoration_total, gifts_total, cookies_total = 0, 0, 0
christmas = False
directins = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
    }
for i in range(rows):
    workshop.append(input().split())
    if "Y" in workshop[i]:
        position = [i, workshop[i].index("Y")]
    decoration_total += workshop[i].count("D")
    gifts_total += workshop[i].count("G")
    cookies_total += workshop[i].count("C")

command = input()
while command != "End":
    command = command.split("-")
    workshop[position[0]][position[1]] = "x"
    move, steps = command[0], int(command[1])

    for i in range(steps):
        current_row = position[0] + directins[move][0]
        current_col = position[1] + directins[move][1]
        position = [current_row, current_col]
        if current_row >= rows:
            current_row -= rows
        if current_col >= cols:
            current_col -= cols
        if current_row < 0 and abs(current_row) >= rows:
            current_row += rows
        if current_col < 0 and abs(current_col) >= cols:
            current_col += cols

        position = [current_row, current_col]
        if workshop[position[0]][position[1]] == "C":
            cookies_collected += 1
        elif workshop[position[0]][position[1]] == "D":
            decoration_collected += 1
        elif workshop[position[0]][position[1]] == "G":
            gifts_collected += 1
        workshop[position[0]][position[1]] = "x"
        if decoration_collected == decoration_total and gifts_collected == gifts_total and cookies_collected == cookies_total:
            workshop[position[0]][position[1]] = "Y"
            print("Merry Christmas!")
            christmas = True
            break
    if christmas:
        break
    workshop[position[0]][position[1]] = "Y"
    command = input()
print(f"You've collected:\n- {decoration_collected} Christmas decorations\n- {gifts_collected} Gifts\n- {cookies_collected} Cookies")    
for row in workshop:
    print(*row)
