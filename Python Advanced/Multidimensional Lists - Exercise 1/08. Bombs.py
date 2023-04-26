matrix_size = int(input())
matrix, alive, sum_alive = [], 0, 0

for row in range(matrix_size):
    matrix.append([int(i) for i in input().split()])
bombs = [[int(j) for j in i.split(",")] for i in input().split()]
for bomb in bombs:
    explosion = matrix[bomb[0]][bomb[1]]
    
    if bomb[0] >= 1:
        if matrix[bomb[0] - 1][bomb[1]] > 0:
            matrix[bomb[0] - 1][bomb[1]] -= explosion
        
        if bomb[1] >= 1 and matrix[bomb[0] - 1][bomb[1] - 1] > 0:
            matrix[bomb[0] - 1][bomb[1] - 1] -= explosion
            
        if bomb[1] < matrix_size - 1 and matrix[bomb[0] - 1][bomb[1] + 1] > 0:    
            matrix[bomb[0] - 1][bomb[1] + 1] -= explosion
    
    if bomb[1] >= 1:
        if matrix[bomb[0]][bomb[1] - 1] > 0:
            matrix[bomb[0]][bomb[1] - 1] -= explosion
        if bomb[0] < matrix_size - 1 and  matrix[bomb[0] + 1][bomb[1] - 1] > 0: 
            matrix[bomb[0] + 1][bomb[1] - 1] -= explosion
    
    if bomb[0] < matrix_size - 1:    
        if matrix[bomb[0] + 1][bomb[1]] > 0:
            matrix[bomb[0] + 1][bomb[1]] -= explosion
        if bomb[1] < matrix_size - 1 and matrix[bomb[0] + 1][bomb[1] + 1] > 0:
            matrix[bomb[0] + 1][bomb[1] + 1] -= explosion
    
    if bomb[1] < matrix_size - 1 and matrix[bomb[0]][bomb[1] + 1] > 0:
        matrix[bomb[0]][bomb[1] + 1] -= explosion
    
    matrix[bomb[0]][bomb[1]] = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive += 1
            sum_alive += el
print(f"Alive cells: {alive}")
print(f"Sum: {sum_alive}")
for row in matrix:
    print(*row)
