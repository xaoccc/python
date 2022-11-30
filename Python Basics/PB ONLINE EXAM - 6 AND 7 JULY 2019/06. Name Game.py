player_name = ""
pts = 0
max_pts = 0
winner = ""
 
while True:
  total_pts = pts
  if total_pts >= max_pts:
    max_pts = total_pts
    winner = player_name
  player_name = input()
  if player_name == "Stop":
    break
  pts = 0
  for i in range(len(player_name)):
    number = int(input())
    if ord(player_name[i]) == number:
      pts += 10
    else:
      pts += 2
print(f"The winner is {winner} with {max_pts} points!")
