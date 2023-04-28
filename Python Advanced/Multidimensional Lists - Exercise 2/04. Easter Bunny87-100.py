matrix_size = int(input())
matrix = []
collected_eggs = {"up": 0, "down": 0, "left": 0, "right": 0}
movement = {"up": [], "down": [], "left": [], "right": []}

for row in range(matrix_size):
    matrix.append([int(i) if i.isdigit() or "-" in i else i for i in input().split()])
    if "B" in matrix[row]:
        bunny_position = [row, matrix[row].index("B")]

#check up
for i in range(bunny_position[0] - 1, -1, -1):
    if matrix[i][bunny_position[1]] != "X":
        collected_eggs["up"] += matrix[i][bunny_position[1]]
        movement["up"].append([i, bunny_position[1]])
    else:
        break
#check down   
for i in range(bunny_position[0] + 1, matrix_size):
    if matrix[i][bunny_position[1]] != "X":
        collected_eggs["down"] += matrix[i][bunny_position[1]]
        movement["down"].append([i, bunny_position[1]])
    else:
        break    
#check left     
for i in range(bunny_position[1] - 1, -1, -1):
    if matrix[bunny_position[0]][i] != "X":
        collected_eggs["left"] += matrix[bunny_position[0]][i]
        movement["left"].append([bunny_position[0], i])
    else:
        break    
#check right
for i in range(bunny_position[1] + 1, matrix_size):
    if matrix[bunny_position[0]][i] != "X":
        collected_eggs["right"] += matrix[bunny_position[0]][i]
        movement["right"].append([bunny_position[0], i])
    else:
        break  

max_direction = list(collected_eggs.keys())[list(collected_eggs.values()).index(max(collected_eggs.values()))]
max_eggs = max(collected_eggs.values())

print(max_direction)
for coord in movement[max_direction]:
    print(coord)
print(max_eggs) 
