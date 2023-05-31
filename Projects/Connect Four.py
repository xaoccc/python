cols, rows = [int(input()), int(input())]
playground = [[0 for j in range(cols)] for i in range(rows)]
visited = []
player_one, player_two = 0, 0

def out_of_playground(row, col):
    if row >= rows or col >= cols or row < 0 or col < 0:
        return True
    return False

i = 0
while True:
    i += 1
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
        else:
            playground[row][col] += 2        
    
    for row in playground:
        print(*row)
