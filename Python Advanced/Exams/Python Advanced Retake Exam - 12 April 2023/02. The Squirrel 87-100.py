map_size = int(input())
directions = input().split(", ")
field_map = []
hazelnuts = 0
trap, fall = False, False
for row in range(map_size):
    field_map.append(list(input()))
    if "s" in field_map[row]:
        squirrel_coordinates = [row, field_map[row].index("s")]
current_position = squirrel_coordinates

for move in directions:
    if move == "up":
        current_position[0] -= 1
    elif move == "down":
        current_position[0] += 1
    elif move == "left":
        current_position[1] -= 1
    elif move == "right":
        current_position[1] += 1
    
    if current_position[0] < 0 or current_position[0] >= map_size or current_position[1] < 0 or current_position[1] >= map_size:
        print("The squirrel is out of the field.")
        fall = True
        break
    
    elif field_map[current_position[0]][current_position[1]] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        trap = True
        break
    
    elif field_map[current_position[0]][current_position[1]] == "h":
        hazelnuts += 1
    
    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break
if not trap and not fall and hazelnuts < 3:
    print(f"There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")
