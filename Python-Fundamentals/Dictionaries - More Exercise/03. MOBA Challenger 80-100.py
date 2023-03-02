command = input()
players_data, total_skills, sorted_data, sorted_total  = {}, {}, {}, {}

def add_players(player, position, skill):
    if player not in players_data:
        players_data[player] = position_skill
    else:
        if position not in players_data[player] or skill > players_data[player][position]:
            players_data[player][position] = skill
            
def duel(player1, player2):
    for position1 in players_data[player1]:
        for position2 in players_data[player2]:
            if position1 == position2:
                if sum(list(players_data[player1].values())) > sum(list(players_data[player2].values())):
                    players_data.pop(player2)
                elif sum(list(players_data[player1].values())) < sum(list(players_data[player2].values())):
                    players_data.pop(player1)
                break

while command != "Season end":
    if " -> " in command:
        position_skill = {}
        player, position, skill = [int(element) if element.isdigit() else element for element in command.split(" -> ")]
        position_skill[position] = skill
        add_players(player, position, skill)
        
    else:
        player1, player2 = command.split(" vs ")
        if player1 in players_data and player2 in players_data:
            duel(player1, player2)

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
