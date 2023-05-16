n = int(input())
hits, cruizers_destroyed = 0, 0
area_map = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
for i in range(n):
    area_map.append(list(input()))
    if "S" in area_map[i]:
        coordinates = [i, area_map[i].index("S")]

while True:
    command = input()
    area_map[coordinates[0]][coordinates[1]] = "-"
    coordinates = [coordinates[0] + directions[command][0], coordinates[1] + directions[command][1]]
    area = area_map[coordinates[0]][coordinates[1]]
    area_map[coordinates[0]][coordinates[1]] = "S"
    if area == "*":
        hits += 1
        if hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{coordinates[0]}, {coordinates[1]}]!")
            break
            
    elif area == "C": 
        cruizers_destroyed += 1
        if cruizers_destroyed == 3:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    
for row in area_map:
    print("".join(row))
