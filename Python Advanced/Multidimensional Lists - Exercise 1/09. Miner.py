mine_size = int(input())
mine_map = []
start_found = False
coal_collected = 0
total_coal = 0
directions = input().split()

for row in range(mine_size):
    mine_map.append(input().split())
    if "s" in mine_map[row] and not start_found:
        start = [row, mine_map[row].index("s")]
        start_found = True
    if "c" in mine_map[row]:
        total_coal += mine_map[row].count("c")
      
current_position = start

for move in directions:
    
    if move == "up" and current_position[0] > 0:
        current_position[0] -= 1
    elif move == "down" and current_position[0] < mine_size - 1:
        current_position[0] += 1
    elif move == "left" and current_position[1] > 0:
        current_position[1] -= 1
    elif move == "right" and current_position[1] < mine_size - 1:
        current_position[1] += 1

    current_element = mine_map[current_position[0]][current_position[1]]

    if current_element == "c":
        coal_collected += 1
        if coal_collected == total_coal:
            print(f"You collected all coal! {tuple(current_position)}")
            break
        mine_map[current_position[0]][current_position[1]] = "*"
    elif current_element == "e":
        print(f"Game over! {tuple(current_position)}")
        break

if coal_collected < total_coal and current_element != "e":
    print(f"{total_coal - coal_collected} pieces of coal left. {tuple(current_position)}")
