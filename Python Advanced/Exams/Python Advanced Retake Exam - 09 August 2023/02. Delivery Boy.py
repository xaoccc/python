directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
rows, cols = [int(i) for i in input().split()]
matrix = []
# Create the matrix
for row in range(rows):
    matrix.append(list(input()))
    if "B" in matrix[row]:
        col = matrix[row].index("B")
        position = [row, col]
        initial_position = [row, col]

while True:
    move = input()

    position = [position[0] + directions[move][0], position[1] + directions[move][1]]

    if position[0] < 0 or position[0] >= rows or position[1] < 0 or position[1] >= cols:
        print("The delivery is late. Order is canceled.")
        matrix[initial_position[0]][initial_position[1]] = " "
        [print("".join(row)) for row in matrix]
        break

    if matrix[position[0]][position[1]] == "*":
        position = [position[0] - directions[move][0], position[1] - directions[move][1]]
        continue

    if matrix[position[0]][position[1]] not in ["P", "R", "A"]:
        matrix[position[0]][position[1]] = "."

    if matrix[position[0]][position[1]] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[position[0]][position[1]] = "R"

    if matrix[position[0]][position[1]] == "A":
        print("Pizza is delivered on time! Next order...")
        matrix[position[0]][position[1]] = "P"
        matrix[initial_position[0]][initial_position[1]] = "B"
        [print("".join(row)) for row in matrix]
        break
