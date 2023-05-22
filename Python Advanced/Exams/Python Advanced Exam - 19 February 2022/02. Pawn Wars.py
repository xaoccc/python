game_map = []
movement = {
    "w": (-1, 0),
    "b": (1, 0)
}
positions_map = {}
letters = [chr(i) for i in range(97, 105)]
for i in range(8, 0, -1):
    positions_map[i] = []
    for j in range(8):
        positions_map[i].append(letters[j] + str(i))
for row in range(8):
    game_map.append(input().split())
    if "b" in game_map[row]:
        black_position = [row, game_map[row].index("b")]
    if "w" in game_map[row]:
        white_position = [row, game_map[row].index("w")]
 
for move in range(16):

    if white_position[0] == 0:
        print(f"Game over! White pawn is promoted to a queen at {positions_map[8-white_position[0]][white_position[1]]}.")
        break
    elif black_position[0] == 7:
        print(f"Game over! Black pawn is promoted to a queen at {positions_map[8-black_position[0]][black_position[1]]}.")
        break
    else:
        if move % 2 == 0:
            if (white_position[0] == black_position[0] - 1 and white_position[1] == black_position[1] - 1) or (white_position[0] == black_position[0] + 1 and white_position[1] == black_position[1] + 1) or (white_position[0] == black_position[0] - 1 and white_position[1] == black_position[1] + 1) or (white_position[0] == black_position[0] + 1 and white_position[1] == black_position[1] - 1):
                print(f"Game over! White win, capture on {positions_map[8-black_position[0]][black_position[1]]}.")
                break
            white_position = [white_position[0] + movement["w"][0], white_position[1]]
        else:
            if (white_position[0] == black_position[0] - 1 and white_position[1] == black_position[1] - 1) or (white_position[0] == black_position[0] + 1 and white_position[1] == black_position[1] + 1) or (white_position[0] == black_position[0] - 1 and white_position[1] == black_position[1] + 1) or (white_position[0] == black_position[0] + 1 and white_position[1] == black_position[1] - 1):
                print(f"Game over! Black win, capture on {positions_map[8-white_position[0]][white_position[1]]}.")
                break
            black_position = [black_position[0]  + movement["b"][0], black_position[1]]
