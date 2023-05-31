directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (-1, 0),
    "right": (1, 0)
}
matrix = []
for i in range(int(input)):
    matrix.append(list(input()))
    if "P" in matrix[i]:
        position = [i, matrix[i].index("P")]
        matrix[position[0]][position[1]] = "unmarked"
     
