command = input()
players_data = {}
total_skills = {}
sorted_data = {}
sorted_total = {}

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
                        if sum(list(players_data[player1].values())) > sum(list(players_data[player2].values())):
                            players_data.pop(player2)
                        elif sum(list(players_data[player1].values())) < sum(list(players_data[player2].values())):
                            players_data.pop(player1)
                        break
    command = input()
    
for player in  players_data:
    total_skills[player] = sum(players_data[player][i] for i in players_data[player])
    sorted_data[player] = dict(sorted(players_data[player].items(), key=lambda y: (-y[1], y[0])))
    
for i in total_skills:
    sorted_total = dict(sorted(total_skills.items(), key=lambda y: (-y[1], y[0])))
    
for i in sorted_total:
    print(f"{i}: {sorted_total[i]} skill")
    for j in sorted_data[i]:
        print(f"- {j} <::> {sorted_data[i][j]}")
