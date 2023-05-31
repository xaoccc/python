
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
matrix = []
# Create the matrix
for i in range(int(input())):
    matrix.append(input().split())
    if "P" in matrix[i]:
        position = [i, matrix[i].index("P")]
        matrix[position[0]][position[1]] = "unmarked"        
       
while True:
    move = input() 
    position = [position[0] + directions[move][0], position[1] + directions[move][1]]
    if position[0] < 0 or position[0] >= len(matrix) or position[1] < 0 or position[1] >= len(matrix):
        # logic for out of the map
    elif:
        # Some other logic
    else:
        # Some more logic

matrix[position[0]][position[1]] = "P"   

# Print the matrix + some other result
for row in matrix:
    print("".join(row))
     
