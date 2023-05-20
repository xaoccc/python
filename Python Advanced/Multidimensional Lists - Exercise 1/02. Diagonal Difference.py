n = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
for i in range(n):
    matrix.append([int(i) for i in input().split()])

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n-i-1])
print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
