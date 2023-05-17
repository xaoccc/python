matrix = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
for i in range(6):
    matrix.append(input().split())
position = [int(i) for i in input()[1:-1].split(", ")]

command = input()
while command != "Stop":
    command = command.split(", ")
    position = [position[0] + directions[command[1]][0], position[1] + directions[command[1]][1]]
    symbol = matrix[position[0]][position[1]]
    
    if command[0] == "Create" and symbol == ".":
        matrix[position[0]][position[1]] = command[2]
    elif command[0] == "Read" and symbol != ".":
        print(symbol)
    elif command[0] == "Update" and symbol != ".":
        matrix[position[0]][position[1]] = command[2]
    elif command[0] == "Delete" and symbol != ".":
        matrix[position[0]][position[1]] = "."        

    command = input()
for row in matrix:
    print(*row)
