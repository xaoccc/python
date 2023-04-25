rows, cols = [int(i) for i in input().split(", ")]
matrix, final_matrix = [], []
max_sum = -1000000

for i in range(rows):
    matrix.append([int(j) for j in input().split(", ")])

for i in range(rows - 1):
    for j in range(cols - 1):
        current_sum = matrix[i][j] + matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            final_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]

print(*final_matrix[:2])
print(*final_matrix[2:])
print(max_sum)
