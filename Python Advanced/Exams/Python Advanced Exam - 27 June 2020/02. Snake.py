map_size, matrix, lair, snake_position, food = int(input()), [], [], [], 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
for row in range(map_size):
    matrix.append(list(input()))
    for col in range(map_size):
        if matrix[row][col] == "S":
            snake_position = [row, col]
        elif matrix[row][col] == "B":
            lair.append([row, col])

while True:
    matrix[snake_position[0]][snake_position[1]] = "."
    move = input()
    snake_position = [snake_position[0] + directions[move][0], snake_position[1] + directions[move][1]]
    if snake_position[0] == map_size or snake_position[1] == map_size or snake_position[0] == -1 or snake_position[1] == -1:
        print("Game over!")
        break
    
    elif matrix[snake_position[0]][snake_position[1]] == "B":
        matrix[snake_position[0]][snake_position[1]] = "."
        if snake_position == lair[0]:
            snake_position = lair[1]
        else:
            snake_position = lair[0]
    elif matrix[snake_position[0]][snake_position[1]] == "*":
        food += 1
        if food == 10:
            matrix[snake_position[0]][snake_position[1]] = "S"
            print("You won! You fed the snake.")
            break


print(f"Food eaten: {food}")
for row in matrix:
    print(''.join(row))
