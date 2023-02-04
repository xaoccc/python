line_one, line_two, line_three = input().split(), input().split(), input().split()
first_win, second_win  = False, False

game_data = line_one + line_two + line_three
game_data = [eval(i) for i in game_data]
for i in range(3):
    if (game_data[i] + game_data[i + 3] + game_data[i + 6] == 6) \
    or (game_data[3 * i] + game_data[(3 * i) + 1] + game_data[(3 * i) + 2] == 6):
        second_win = True
    elif (game_data[i] == 1 and game_data[i + 3] == 1 and game_data[i + 6] == 1) \
    or (game_data[3 * i] == 1 and game_data[(3 * i) + 1] == 1 and game_data[(3 * i) + 2] == 1):
        first_win = True
if (game_data[0] + game_data[4] + game_data[8] == 6) \
or (game_data[2] + game_data[4] + game_data[6] == 6):
    second_win = True
if (game_data[0] == 1 and game_data[4] == 1 and game_data[8] == 1) \
or (game_data[2] == 1 and game_data[4] == 1 and game_data[6] == 1):
    first_win = True
    
if first_win == True and second_win == True:
    print("Draw!")
elif first_win == True:
    print("First player won")
elif second_win == True:
    print("Second player won")
else:
    print("Draw!")
