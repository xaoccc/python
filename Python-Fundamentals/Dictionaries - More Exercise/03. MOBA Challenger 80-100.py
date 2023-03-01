command = input()
players_data = {}
total_skills = {}
sorted_data = {}

#checking for commands
while command != "Season end":
    if " -> " in command:
        #Creating players data
        command = command.split(" -> ")
        position_skill = {}
        player = command[0]
        position = command[1]
        skill = int(command[2])
        #Creating a dictionary for each skill and epmty it at the beginning of each loop
        position_skill[position] = skill
        #If the player is not in the dictionary, we insert its data
        if player not in players_data:
            players_data[player] = position_skill
        else:
            #If the player is in the dictionary, but his position is not or his skill is less than new skill, we update the info
            if position not in players_data[player] or skill > players_data[player][position]:
                players_data[player][position] = skill
        
    else:
        #We receive the fight info
        command = command.split(" vs ")
        player1 = command[0]
        player2 = command[1]
        #We check if both players exist and ...
        if player1 in players_data and player2 in players_data:
            for position1 in players_data[player1]:
                for position2 in players_data[player2]:
                    #...if there is at least one common position
                    if position1 == position2:
                        #Entirely remove the player with smaller sum of all skills
                        if sum(list(players_data[player1].values())) > sum(list(players_data[player2].values())):
                            players_data.pop(player2)
                        elif sum(list(players_data[player1].values())) < sum(list(players_data[player2].values())):
                            players_data.pop(player1)
                        break
    command = input()

#We need 2 more dictionaries - 1 for skills sum of each player and 1 for the sorted list of all data    
for player in  players_data:
    total_skills[player] = sum(players_data[player][i] for i in players_data[player])
    sorted_data[player] = dict(sorted(players_data[player].items(), key=lambda y: -y[1]))
    
#We create 1 more dicionary to sort the summed skills    
for i in total_skills:
    sorted_total = dict(sorted(total_skills.items(), key=lambda y: -y[1]))

#Print the output
for i in sorted_total:
    print(f"{i}: {sorted_total[i]} skill")
    for j in sorted_data[i]:
        print(f"- {j} <::> {sorted_data[i]}")
        
        

