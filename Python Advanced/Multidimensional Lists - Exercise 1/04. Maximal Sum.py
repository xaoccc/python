rows, cols = [int(i) for i in input().split()]
matrix, result, max_sum = [], [], -100000

for i in range(rows):
    matrix.append([int(i) for i in input().split()])

for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 2][j] + matrix[i][j + 2] + matrix[i + 1][j + 2] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
        if  current_sum > max_sum:
            max_sum = current_sum
            result = [[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]], [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]], [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]]
print(f"Sum = {max_sum}")
for row in result:
    print(*row)
