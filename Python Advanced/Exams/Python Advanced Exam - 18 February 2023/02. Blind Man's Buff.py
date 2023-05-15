# unput map size
n, m = [int(i) for i in input().split()]
# We need 4 variables - map, number of touched people, number or moves and directions
playground, touched, moves = [], 0, 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

# Draw the map and get the starting player position
for i in range(n):
    playground.append(input().split())
    if "B" in playground[i]:
        player_location = [i, playground[i].index("B")]

command = input()
while command != "Finish":
  # If we are here it means there ia s move and the player position has changed. We mark current tile as visited and available for move
    playground[player_location[0]][player_location[1]] = "-"
    # Get the next player position by using the directions dicionary
    player_location = [player_location[0] + directions[command][0], player_location[1] + directions[command][1]]
    # if the position is invalid, we return. Again by using directions dictionary, but this time reversed. So player has returned on his last position and we mark tis on the map.
    if player_location[0] < 0 or player_location[0] >= n or player_location[1] < 0 or player_location[1] >= m or playground[player_location[0]][player_location[1]] == "O":
            player_location = [player_location[0] - directions[command][0], player_location[1] - directions[command][1]]
            playground[player_location[0]][player_location[1]] = "B"
    # If we touch another player, remove him from the map, the main player takes his plase, we increase the number of touched people, as well as number or moves by one
    elif playground[player_location[0]][player_location[1]] == "P":
        playground[player_location[0]][player_location[1]] = "B"
        touched += 1
        moves += 1
        # If we reach our target, we exit the loop
        if touched == 3:
            break
    # If we reach valid free spot, we mark it as current position and increase the number or moves by one 
    elif playground[player_location[0]][player_location[1]] == "-":
        playground[player_location[0]][player_location[1]] = "B"
        moves += 1
    command = input()

#Output
print(f"Game over!\nTouched opponents: {touched} Moves made: {moves}")
