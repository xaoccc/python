map_size, mines = int(input()), int(input())
map = []

def check_for_mines(mines):
    start_row = row - 1
    if start_row < 0:
        start_row = 0
        
    end_row = row + 1
    if end_row == map_size:
        end_row = map_size - 1
        
    start_col = col - 1
    if start_col < 0:
        start_col = 0
        
    end_col = col + 1
    if end_col == map_size:
        end_col = map_size - 1
        
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if map[i][j] == "*":
                mines += 1
    map[row][col] = mines

for i in range(map_size):
    map.append([0] * map_size)
 
for i in range(mines):
    mine_coordinates = [int(i) for i in input()[1:-1].split(", ")]
    map[mine_coordinates[0]][mine_coordinates[1]] = "*"

for row in range(map_size):
    for col in range(map_size):
        if map[row][col] != "*":
            check_for_mines(0)

for row in map:
    print(*row)
