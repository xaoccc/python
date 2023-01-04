line_one = input()
line_two = input()
line_three = input()

line_one = line_one.split(" ")
line_two = line_two.split(" ")
line_three = line_three.split(" ")

game_data = line_one + line_two + line_three
game_data = [eval(i) for i in game_data]

if (game_data[0] + game_data[3] + game_data[6] == 6) \n
    or (game_data[1] + game_data[4] + game_data[7] == 6) \n
    or (game_data[2] + game_data[5] + game_data[8] == 6) \n
    
    or (game_data[0] + game_data[1] + game_data[2] == 6) \n
    or (game_data[3] + game_data[4] + game_data[5] == 6) \n
    or (game_data[6] + game_data[7] + game_data[8] == 6) \n
    
    or (game_data[0] + game_data[4] + game_data[8] == 6) \n
    or (game_data[2] + game_data[4] + game_data[6] == 6):

    print("Second player won")

elif

print(game_data)
