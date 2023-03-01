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
        player1 = command[0]
        player2 = command[1]
        if player1 in players_data and player2 in players_data:
            for position1 in players_data[player1]:
                for position2 in players_data[player2]:
                    if position1 == position2:
                        if players_data[player1][position1] > players_data[player2][position2]:
                            players_data.pop(player2)
                        elif players_data[player1][position1] < players_data[player2][position2]:
                            players_data.pop(player1)
                        break
                            
    
    print(players_data)
        
        
    command = input()
