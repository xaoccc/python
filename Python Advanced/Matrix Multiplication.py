matrix_size = int(input("Enter matrices size: "))

matrix_one = [[int(i) for i in input().split()] for j in range(matrix_size)]
matrix_two = [[int(i) for i in input().split()] for j in range(matrix_size)]
result = [[0 for i in range(matrix_size)] for j in range(matrix_size)]

for i in range(len(matrix_one)):
    for j in range(len(matrix_two[0])):
        for k in range(len(matrix_two)):
            result[i][j] += matrix_one[i][k] * matrix_two[k][j]

print(result)