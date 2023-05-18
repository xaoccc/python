from collections import deque
tj = deque(input().split(", "))

turn = 0
area_map = []
rest = False
both_rest = False

for row in range(6):
    area_map.append(input().split())

while True:
    coordinates = [int(i) for i in input()[1:-1].split(", ")]
    if both_rest == True:
        both_rest = False
        continue

    if area_map[coordinates[0]][coordinates[1]] == "W":
        print(f"{tj[turn]} hits a wall and needs to rest.")
        if rest == True:
            both_rest = True
            rest = False
            continue
        rest = True
        

    elif area_map[coordinates[0]][coordinates[1]] == "T":
        print(f"{tj[turn]} is out of the game! The winner is {tj[turn - 1]}." )
        break
    elif area_map[coordinates[0]][coordinates[1]] == "E":
        print(f"{tj[turn]} found the Exit and wins the game!")
        break

    turn += 1
    if turn == 2:
        turn = 0
