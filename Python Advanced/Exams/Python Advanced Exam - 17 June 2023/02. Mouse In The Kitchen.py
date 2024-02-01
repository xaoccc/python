

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
matrix = []

rows, cols = [int(i) for i in input().split(",")]
total_cheese_on_map = 0
collected_cheese = 0

for row in range(rows):
    matrix.append(list(input()))

    for col in range(cols):
        if "M" in matrix[row]:
            start = [row, matrix[row].index("M")]

    if "C" in matrix[row]:
        total_cheese_on_map += matrix[row].count("C")

current_position = start

command = input()
while command != "danger":

    if current_position[0] + directions[command][0] >= rows or current_position[1] + directions[command][1] >= cols:
        matrix[current_position[0]][current_position[1]] = "M"
        print("No more cheese for tonight!")
        [print("".join(row)) for row in matrix]
        break

    if matrix[current_position[0] + directions[command][0]][current_position[1] + directions[command][1]] == "@":
        command = input()
        continue

    matrix[current_position[0]][current_position[1]] = "*"

    current_position[0] += directions[command][0]
    current_position[1] += directions[command][1]

    if matrix[current_position[0]][current_position[1]] == "C":
        collected_cheese += 1
        if collected_cheese == total_cheese_on_map:
            matrix[current_position[0]][current_position[1]] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            [print("".join(row)) for row in matrix]
            break

    if matrix[current_position[0]][current_position[1]] == "T":
        matrix[current_position[0]][current_position[1]] = "M"
        print("Mouse is trapped!")
        [print("".join(row)) for row in matrix]
        break
    command = input()

if command == "danger" and collected_cheese < total_cheese_on_map:
    matrix[current_position[0]][current_position[1]] = "M"
    print("Mouse will come back later!")
    [print("".join(row)) for row in matrix]

