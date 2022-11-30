player1 = input()
player2 = input()
game = ""
player1_pts = 0
player2_pts = 0
while game != "End of game":
    player1_card = input()
    if player1_card == "End of game":
        print(f"{player1} has {player1_pts} points")
        print(f"{player2} has {player2_pts} points")
        break
    player2_card = input()
 
    if int(player1_card) > int(player2_card):
        player1_pts += int(player1_card) - int(player2_card)
    elif int(player2_card) > int(player1_card):
        player2_pts += int(player2_card) - int(player1_card)
    else:
        player1_card2 = int(input())
        player2_card2 = int(input())    
        if player1_card2 > player2_card2:
            print("Number wars!")
            print(f"{player1} is winner with {player1_pts} points")
        else:
            print("Number wars!")
            print(f"{player2} is winner with {player2_pts} points")
        break
