rows, cols = [int(i) for i in input().split()]
matrix, result, max_sum = [], [], -100000

for i in range(rows):
    matrix.append([int(i) for i in input().split()])

for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = sum(matrix[i][j:j+3]) + sum(matrix[i+1][j:j+3]) + sum(matrix[i+2][j:j+3])
        if  current_sum > max_sum:
            max_sum = current_sum
            result = [matrix[i][j:j+3], matrix[i+1][j:j+3], matrix[i+2][j:j+3]]
print(f"Sum = {max_sum}")
for row in result:
    print(*row)
