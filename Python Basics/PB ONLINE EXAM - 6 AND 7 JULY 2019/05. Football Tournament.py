team_name = input()
games_num = int(input())
if games_num == 0:
    print(f"{team_name} hasn't played any games during this season.")
total_pts = 0
wins_num = 0
d_num = 0
loss_num = 0
 
for i in range(games_num):
    result = input()
    if result == "W":
        wins_num += 1
        total_pts += 3
    elif result == "D":
        d_num += 1
        total_pts += 1
    elif result == "L":
        loss_num += 1
if games_num > 0:
    print(f"{team_name} has won {total_pts} points during this season.")
    print("Total stats:")
    print(f"## W: {wins_num}")
    print(f"## D: {d_num}")
    print(f"## L: {loss_num}")
    print(f"Win rate: {wins_num * 100 / games_num:.2f}%")
