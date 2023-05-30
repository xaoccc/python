matrix_size = int(input())
matrix, path = [], []
coins_collected = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for i in range(matrix_size):
    matrix.append([int(i) if i.isdigit() else i for i in input().split()])
    if "P" in matrix[i]:
        position = [i, matrix[i].index("P")]
matrix[position[0]][position[1]] = 0
path.append(position)   
while True:
    command = input()
    if command in directions:
        position = [position[0] + directions[command][0], position[1] + directions[command][1]]
    else:
        continue
    
    if position[0] < 0:
        position[0] += matrix_size
    if position[1] < 0:
        position[1] += matrix_size
    if position[0] >= matrix_size:
        position[0] -= matrix_size
    if position[1] >= matrix_size:
        position[1] -= matrix_size
    
    path.append(position)
    if matrix[position[0]][position[1]] == "X":
        print(f"Game over! You've collected {coins_collected // 2} coins.\nYour path:")
        break
    else:
        coins_collected += matrix[position[0]][position[1]]
        matrix[position[0]][position[1]] = 0
    
    if coins_collected >= 100:
        print(f"You won! You've collected {coins_collected} coins.\nYour path:")
        break

for i in path:
    print(i)
