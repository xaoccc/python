player_one, player_two = input().split(", ")
scores = {
    player_one: [501, 0],
    player_two: [501, 0],
}
darts, hit = [], 0
for i in range(7):
    darts.append([int(i) if i.isdigit() else i for i in input().split()])

while True:
    throw = [int(i) for i in input()[1:-1].split(", ")]
    hit += 1
    if hit % 2 != 0:
        player = player_one
    elif hit % 2 == 0:
        player = player_two
    scores[player][1] += 1
    
    if throw[0] < 0 or throw[0] > 6 or throw[1] < 0 or throw[1] > 6:
        continue
    hit_sector = darts[throw[0]][throw[1]]
    if type(hit_sector) is int:
        scores[player][0] -= hit_sector
   
    elif hit_sector == "D":
        scores[player][0] -= (darts[throw[0]][0] + darts[throw[0]][-1] + darts[0][throw[1]] + darts[-1][throw[1]]) * 2
   
    elif hit_sector == "T":
        scores[player][0] -= (darts[throw[0]][0] + darts[throw[0]][-1] + darts[0][throw[1]] + darts[-1][throw[1]]) * 3
   
    elif hit_sector == "B":
        scores[player][0] -= 501
   
    if scores[player][0] <= 0:
        print(f"{player} won the game with {scores[player][1]} throws!")
        break 
