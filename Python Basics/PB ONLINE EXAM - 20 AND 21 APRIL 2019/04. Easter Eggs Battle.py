eggs_player1 = int(input())
eggs_player2 = int(input())
wins_player1 = 0
wins_player2 = 0
while eggs_player1 > 0 and eggs_player2 > 0:
    action = input()
    if action == "one":
        wins_player1 += 1
        eggs_player2 -= 1
    elif action == "two":
        wins_player2 += 1
        eggs_player1 -= 1
    if action == "End":
        print(f"Player one has {eggs_player1} eggs left.")
        print(f"Player two has {eggs_player2} eggs left.")
        break
if eggs_player1 == 0:
    print(f"Player one is out of eggs. Player two has {eggs_player2} eggs left.")
elif eggs_player2 == 0:
    print(f"Player two is out of eggs. Player one has {eggs_player1} eggs left.")
