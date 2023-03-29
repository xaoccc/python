command = input()
cardtype = {"S": 4, "H": 3, "D": 2, "C": 1}
power = {"J": 11, "Q": 12, "K": 13, "A": 14}

players_decks = {}
while command != "JOKER":
    command = command.split(": ")
    player = command[0]
    current_deck = command[1].split(", ")
    if player not in players_decks:
        players_decks[player] = current_deck
    else:
        players_decks[player] += current_deck
    command = input()
for player, deck in players_decks.items():
    players_decks[player] = list(set(deck))

for player, deck in players_decks.items():
    score = 0
    for i in deck:
        if i[0].isdigit():
            score += int(i[:-1]) * cardtype[i[-1]]
        else:
            score += power[i[0]] * cardtype[i[-1]]
    print(f"{player}: {score}")
