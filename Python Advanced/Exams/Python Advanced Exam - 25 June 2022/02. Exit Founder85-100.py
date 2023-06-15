player_one, player_two = input().split(", ")
matrix = []

for row in range(6):
    matrix.append(input().split())
tom_wall, jerry_wall = False, False

while True:
    move = [int(i) for i in input()[1:-1].split(", ")]
    if tom_wall and jerry_wall:
        if player_one == "Tom":
            tom_wall = False
        elif player_one == "Jerry":
            jerry_wall = False
        continue
    
    if tom_wall and not jerry_wall:
        if player_one == "Tom":
            tom_wall = False
        player_one = "Jerry"
        player_two = "Tom"
    
    if jerry_wall and not tom_wall:
        if player_one == "Jerry":
            jerry_wall = False
        player_one = "Tom"
        player_two = "Jerry"

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
