tournament_name = ""
desi_win = 0
desi_loss = 0
total_games_num = 0
 
while True:
  tournament_name = input()
  if tournament_name == "End of tournaments":
    print(f"{(desi_win / total_games_num) * 100:.2f}% matches win")
    print(f"{(desi_loss / total_games_num) * 100:.2f}% matches lost")
    break   
  games_num = int(input())
  total_games_num += games_num
  game_count = 0
 
  for i in range(games_num):
    desi_team_pts = int(input())
    other_team_pts = int(input())
    game_count += 1
    if desi_team_pts > other_team_pts:
      desi_win += 1
      print(f"Game {game_count} of tournament {tournament_name}: win with {desi_team_pts - other_team_pts} points.")
    else:
      desi_loss += 1
      print(f"Game {game_count} of tournament {tournament_name}: lost with {other_team_pts - desi_team_pts} points.")
