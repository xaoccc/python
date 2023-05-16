n = int(input())
racing_number = input() 
distance = 0
track = []
t1, t2 = [], []
finish = False
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(n):
    track.append(input().split())
    for col in range(n):
        if not t1 and track[row][col] == "T":
            t1 = [row, col]
        if t1 and track[row][col] == "T":
            t2 = [row, col]

position = [0, 0]
command = input()
while command != "End":
    distance += 10
    track[position[0]][position[1]] = "."
    position = [position[0] + directions[command][0], position[1] + directions[command][1]]
    if track[position[0]][position[1]] == "F":
        finish = True
        break
    if position == t1 or position == t2:
        distance += 20
        track[t1[0]][t1[1]] = "."
        track[t2[0]][t2[1]] = "."
    if position == t1:
        position = t2
    elif position == t2:
        position = t1

    command = input()
    
track[position[0]][position[1]] = "C"
if not finish:
    print(f"Racing car {racing_number} DNF.")
else:
    print(f"Racing car {racing_number} finished the stage!")
print(f"Distance covered {distance} km.")
for row in track:
    print("".join(row))
