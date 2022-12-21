cards = input()
cards_list = cards.split(" ")
cards_list_team_a = []
cards_list_team_b = []
for i in range(len(cards_list)):
  if cards_list[i].count("A") > 0:
    cards_list_team_a.append(cards_list[i])
  if cards_list[i].count("B") > 0:
    cards_list_team_b.append(cards_list[i])
  cards_list_team_a = list(dict.fromkeys(cards_list_team_a))
  cards_list_team_b = list(dict.fromkeys(cards_list_team_b))

  if len(cards_list_team_a) == 5 or len(cards_list_team_b) == 5:
    break

print(f"Team A - {11-len(cards_list_team_a)}; Team B - {11-len(cards_list_team_b)}")

if len(cards_list_team_a) == 5 or len(cards_list_team_b) == 5:
  print(f"Game was terminated")
