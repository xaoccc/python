all_players, current_sort, total = {}, {}, {}
command = input()
while command != "Season end":
    if " vs " in command:
        command = command.split(" vs ")
        player_1 = command[0]
        player_2 = command[1]
        if player_1 in all_players.keys() and player_2 in all_players.keys():
            for position, skill in all_players[player_1].items():
                if position in all_players[player_2].keys():
                    if all_players[player_1][position] > all_players[player_2][position]:
                        del all_players[player_2]
                        break
                    if all_players[player_1][position] < all_players[player_2][position]:
                        del all_players[player_1]
                        break
        
    else:
        command = command.split(" -> ")
        player = command[0]
        position = command[1]
        skill = int(command[2])
        if player not in all_players.keys():
            all_players[player] = {position: skill}
        else:
            if position not in all_players[player].keys() or position in all_players[player].keys() and all_players[player][position] < skill:
                all_players[player][position] = skill
        
    command = input()
for player, player_data in all_players.items():
    total[player] = sum(player_data.values())
total = dict(sorted(total.items(), key=lambda x: -x[1]))

for player_name, player_stats in total.items():
    print(f"{player_name}: {player_stats} skill")
    current_sort = dict(sorted(all_players[player_name].items(), key=lambda y: (-y[1], y[0])))
    for position, skill in current_sort.items():
        print(f"- {position} <::> {skill}")
