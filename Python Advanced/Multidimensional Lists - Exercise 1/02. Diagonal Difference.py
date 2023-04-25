n = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
for i in range(n):
    matrix.append([int(i) for i in input().split()])

for i in range(n):
    for j in range(n-1, -1, -1):
        primary_diagonal.append(matrix[i][i])
        secondary_diagonal.append(matrix[i][j-i])
        break
print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
