rows, cols = [int(i) for i in input().split()]
lair_map = []
escaped = False
killed = False

for row in range(rows):
    lair_map.append(list(input()))
    if "P" in lair_map[row]:
        start_coordinates = [row, lair_map[row].index("P")]
moves = input()
def rabbit_move(move):
    if move == "U":
        current_position[0] -= 1
    elif move == "D":
        current_position[0] += 1
    elif move == "L":
        current_position[1] -= 1
    elif move == "R":
        current_position[1] += 1
    return current_position
    
current_position = start_coordinates
for move in moves:
    lair_map[current_position[0]][current_position[1]] = "."
    rabbit_move(move)
    
    for row in range(rows):
        for col in range(cols):
            if lair_map[row][col] == "B":
                if row < rows -1 and lair_map[row + 1][col] != "B":
                    lair_map[row + 1][col] = "C"
                if row > 0 and lair_map[row - 1][col] != "B":
                    lair_map[row - 1][col] = "C"
                if col > 0 and lair_map[row][col - 1] != "B":
                    lair_map[row][col - 1] = "C"
                if col < cols -1 and lair_map[row][col + 1] != "B":
                    lair_map[row][col + 1] = "C"

    for row in range(rows):
        for col in range(cols):  
            if lair_map[row][col] == "C":
                lair_map[row][col] = "B"
                
    if 0 > current_position[0] or current_position[0] >= rows or 0 > current_position[1] or current_position[1] >= cols:
        if move == "U":
            current_position[0] += 1
        elif move == "D":
            current_position[0] -= 1
        elif move == "L":
            current_position[1] += 1
        elif move == "R":
            current_position[1] -= 1
        escaped = True
        break
    elif lair_map[current_position[0]][current_position[1]] == "B":
        killed = True
        break

for row in lair_map:
    print(''.join(row))  
    
if escaped:
    print(f"won: {' '.join([str(i) for i in current_position])}")
elif killed:
    print(f"dead: {' '.join([str(i) for i in current_position])}")
