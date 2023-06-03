
def mark_red(matrix, row, col):
    
    if row < 0 or row >= rows or col < 0 or col >= cols:
        return
    
    if matrix[row][col] != "y":
        return
    
    if matrix[row][col] == "y":
        matrix[row][col] = "red"

    mark_red(matrix, row - 1, col)
    mark_red(matrix, row, col - 1)
    mark_red(matrix, row + 1, col)
    mark_red(matrix, row, col + 1)
    
    return matrix


rows = 6
cols = 7
matrix = []
for i in range(rows):
    matrix.append(input().split())


current = ([int(i) for i in input().split()])
mark_red(matrix, current[0], current[1])

for row in matrix:
    print(*row)