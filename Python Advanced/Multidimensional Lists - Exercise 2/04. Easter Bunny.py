matrix_size = int(input())
matrix = []
collected_eggs = {"up": 0, "down": 0, "left": 0, "right": 0}
movement = {
    "up": [], 
    "down": [], 
    "left": [], 
    "right": []
}

for row in range(matrix_size):
    matrix.append([int(i) if i.isdigit() or "-" in i else i for i in input().split()])
    if "B" in matrix[row]:
        bunny_position = [row, matrix[row].index("B")]
        
        
def move(start, end, step, direction):
    if direction == "up" or direction == "down":
        for i in range(start, end, step):
            if matrix[i][bunny_position[1]] != "X":
                collected_eggs[direction] += matrix[i][bunny_position[1]]
                movement[direction].append([i, bunny_position[1]])
            else:
                break
    else:
        for i in range(start, end, step):
            if matrix[bunny_position[0]][i] != "X":
                collected_eggs[direction] += matrix[bunny_position[0]][i]
                movement[direction].append([bunny_position[0], i])
            else:
                break

move(bunny_position[0] - 1, -1, -1, "up")
move(bunny_position[0] + 1, matrix_size, 1, "down")
move(bunny_position[1] - 1, -1, -1, "left")
move(bunny_position[1] + 1, matrix_size, 1, "right")

#remove empty routes
for key, value in movement.items():
    if not value:
        del collected_eggs[key]

max_direction = list(collected_eggs.keys())[list(collected_eggs.values()).index(max(collected_eggs.values()))]
max_eggs = max(collected_eggs.values())

print(max_direction)
for coord in movement[max_direction]:
    print(coord)
print(max_eggs)
