command = input()
players_data = {}


while command != "Season end":
    if " -> " in command:
        command = command.split(" -> ")
        position_skill = {}
        player = command[0]
        position = command[1]
        skill = int(command[2])
        position_skill[position] = skill
        if player not in players_data:
            players_data[player] = position_skill
        else:
            if position not in players_data[player] or skill > players_data[player][position]:
                players_data[player][position] = skill
        
    else:
        command = command.split(" vs ")
    
    print(players_data)
        
        
    command = input()
