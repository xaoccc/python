word = input()
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []
for i in range(int(input())):
    matrix.append(list(input()))
    if "P" in matrix[i]:
        position = [i, matrix[i].index("P")]
        matrix[position[0]][position[1]] = "-"        
       
for i in range(int(input())):
    move = input() 
    position = [position[0] + directions[move][0], position[1] + directions[move][1]]
    if position[0] < 0 or position[0] >= len(matrix) or position[1] < 0 or position[1] >= len(matrix):
        position = [position[0] - directions[move][0], position[1] - directions[move][1]]
        if len(word) > 0:
            word = word[:-1]
    elif matrix[position[0]][position[1]] == "-" or matrix[position[0]][position[1]].isdigit():
        continue
    else:
        word += matrix[position[0]][position[1]]
        matrix[position[0]][position[1]] = "-"

matrix[position[0]][position[1]] = "P"   
print(word)
for row in matrix:
    print("".join(row))
