presents, n = int(input()), int(input())
neigh_map, good_kids, good_kids_with_presents, cookies = [], 0, 0, 0

for i in range(n):
    neigh_map.append(input().split())
    if "S" in neigh_map[i]:
        santa = [i, neigh_map[i].index("S")]
    if "V" in neigh_map[i]:
        good_kids += neigh_map[i].count("V")
    if "C" in neigh_map[i]:
        cookies += neigh_map[i].count("C")
  
directions = {
    "up": (-1, 0), 
    "down": (1, 0), 
    "left": (0, -1),  
    "right": (0, 1),
    }
command = input()
while True:
    if command == "Christmas morning":
        break
    neigh_map[santa[0]][santa[1]] = "-"
    santa[0], santa[1] = santa[0] + directions[command][0], santa[1] + directions[command][1]
    
    if neigh_map[santa[0]][santa[1]] == "C":
        if (neigh_map[santa[0] - 1][santa[1]] == "X" or neigh_map[santa[0] - 1][santa[1]] == "V") and presents >= 1:
            if neigh_map[santa[0] - 1][santa[1]] == "V":
                good_kids_with_presents += 1
            presents -= 1
            neigh_map[santa[0] - 1][santa[1]] = "-"
        if (neigh_map[santa[0] + 1][santa[1]] == "X" or neigh_map[santa[0] + 1][santa[1]] == "V") and presents >= 1:
            if neigh_map[santa[0] + 1][santa[1]] == "V":
                good_kids_with_presents += 1
            presents -= 1
            neigh_map[santa[0] + 1][santa[1]] = "-"
        if (neigh_map[santa[0]][santa[1] - 1] == "X" or neigh_map[santa[0]][santa[1] - 1] == "V") and presents >= 1:
            if neigh_map[santa[0]][santa[1] - 1] == "V":
                good_kids_with_presents += 1
            presents -= 1
            neigh_map[santa[0]][santa[1] - 1] = "-"
        if (neigh_map[santa[0]][santa[1] + 1] == "X" or neigh_map[santa[0]][santa[1] + 1] == "V") and presents >= 1:
            if neigh_map[santa[0]][santa[1] + 1] == "V":
                good_kids_with_presents += 1
            presents -= 1
            neigh_map[santa[0]][santa[1] + 1] = "-"
            
    elif neigh_map[santa[0]][santa[1]] == "V":
        if presents > 0:
            presents -= 1
            good_kids_with_presents += 1
            if good_kids_with_presents == good_kids:
                neigh_map[santa[0]][santa[1]] = "S"
                for row in neigh_map:
                    print(*row)
                print(f"Good job, Santa! {good_kids} happy nice kid/s.")
                break
    neigh_map[santa[0]][santa[1]] = "S"
    if presents == 0:
        break
    command = input()
    
if good_kids_with_presents != good_kids:
    print("Santa ran out of presents!")
    for row in neigh_map:
        print(*row)
    print(f"No presents for {good_kids - good_kids_with_presents} nice kid/s.")
