rows, cols = [int(i) for i in input().split()]
matrix, result = [], 0

for i in range(rows):
    matrix.append(input().split())

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]:
            result += 1
print(result)
