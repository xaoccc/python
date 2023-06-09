import random
choices = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

while True:
    player_choice = input("Choose[r]ock, [p]aper or [s]cissors :")
    if player_choice in choices.keys():
        player_move = choices[player_choice]

    else:
        print("Invalid input. Please try again...")
        continue
        
    computer_move = choices[list(choices.keys())[random.randint(0, 2)]]
    print(f"The computer chose {computer_move}.")
        
    if (player_move == "Rock" and computer_move == "Scissors") or \
        (player_move == "Paper" and computer_move == "Rock") or \
        (player_move == "Scissors" and computer_move == "Paper"):
        print("You win!")
        
    elif player_move == computer_move:
        print("Draw!")

    else:
        print("You lose!")
    
    if not input("Press [Enter] to play again or press any letter to quit."):
        continue
    else:
        print("Thank you for playing.")
        break
