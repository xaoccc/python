cols, rows = [int(input()), int(input())]
playground = [[0 for j in range(cols)] for i in range(rows)]
player_one, player_two = 0, 0

def find_area(row, col, playground, player):
    if row >= rows or col >= cols or row < 0 or col < 0:
        return 0

    if playground[row][col] != player:
        return 0

    playground[row][col] = player
    area = 1
    area += find_area(row + 1, col, playground, player)
    area += find_area(row - 1, col, playground, player)
    area += find_area(row, col + 1, playground, player)
    area += find_area(row, col - 1, playground, player)
    return area

i = 0
while True:
    i += 1
    coords = [int(i) for i in input().split()]
    row = coords[0]
    col = coords[1]
    if row >= 0 and row < rows and col >= 0 and col < cols:
        if i % 2 != 0:
            playground[row][col] = 1
            print(find_area(row, col, playground, playground[row][col]))
        elif i % 2 == 0:
            playground[row][col] = 2
            print(find_area(row, col, playground, playground[row][col]))
    for row in playground:
        print(*row)
