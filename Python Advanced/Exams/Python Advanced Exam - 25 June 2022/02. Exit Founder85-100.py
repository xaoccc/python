player_one, player_two = input().split(", ")
matrix = []

for row in range(6):
    matrix.append(input().split())
tom_wall, jerry_wall = False, False

while True:
    move = [int(i) for i in input()[1:-1].split(", ")]

    if player_one == "Tom" and tom_wall:
        tom_wall = False
        player_one, player_two = player_two, player_one
        continue
    
    if player_one == "Jerry" and jerry_wall:
        jerry_wall = False
        player_one, player_two = player_two, player_one
        continue      
    
    if matrix[move[0]][move[1]] == "T":
        print(f"{player_one} is out of the game! The winner is {player_two}.")
        break
    elif matrix[move[0]][move[1]] == "E":
        print(f"{player_one} found the Exit and wins the game!" )
        break
    elif matrix[move[0]][move[1]] == "W":
        print(f"{player_one} hits a wall and needs to rest.")
        if player_one == "Tom":
            tom_wall = True
        else:
            jerry_wall = True

    player_one, player_two = player_two, player_one
