matrix = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
deposits = {
    "W": [0, "Water"],
    "M": [0, "Metal"],
    "C": [0, "Concrete"]
}
        
for i in range(6):
    matrix.append(input().split())
    if "E" in matrix[i]:
        coordinates = [i, matrix[i].index("E")]
movement = input().split(", ")

for move in movement:
    matrix[coordinates[0]][coordinates[1]] = "-"
    coordinates = [coordinates[0] + directions[move][0], coordinates[1] + directions[move][1]]
    if coordinates[0] == -1:
        coordinates[0] = 5
    elif coordinates[0] == 6:
        coordinates[0] = 0
    if coordinates[1] == -1:
        coordinates[1] = 5
    elif coordinates[1] == 6:
        coordinates[1] = 0
        
    current_spot = matrix[coordinates[0]][coordinates[1]]
    if current_spot in deposits:
        deposits[current_spot][0] += 1
        print(f"{deposits[current_spot][1]} deposit found at ({coordinates[0]}, {coordinates[1]})")
    elif current_spot == "R":
        print(f"Rover got broken at ({coordinates[0]}, {coordinates[1]})")
        break
    
if deposits["W"][0] > 0 and deposits["M"][0] > 0 and deposits["C"][0] > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
