cols, rows = [int(input()), int(input())]
playground = [[0 for j in range(cols)] for i in range(rows)]
visited = []

directions = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}

def out_of_playground(row, col):
    if row >= rows or col >= cols or row < 0 or col < 0:
        return True
    return False

i = 0
while True:
    i += 1
    player_one, player_two = 0, 0
    coords = [int(i) for i in input().split()]
    row = coords[0]
    col = coords[1]
    if out_of_playground(row, col) or coords in visited:
        print("Invalid coordinates!")
        continue
    else:
        visited.append(coords)
        if i % 2 != 0:
            playground[row][col] += 1
            player_one += 1
            for j in directions.keys():
                current_row, current_col = row + directions[j][0], col + directions[j][1]
                if out_of_playground(current_row, current_col):
                    continue
                if playground[current_row][current_col] == 1:
                    player_one += 1
                    if player_one == 4:
                        break
            
        else:
            playground[row][col] += 2
            player_two += 1
            for j in directions.keys():
                current_row, current_col = row + directions[j][0], col + directions[j][1]
                if out_of_playground(current_row, current_col):
                    continue
                if playground[current_row][current_col] == 2:
                    player_two += 1
                    if player_two == 4:
                        break
            
        
        if player_one == 4:
            print("Player one wins!")
        elif player_two == 4:
            print("Player two wins!")
        
    
    for row in playground:
        print(*row)
