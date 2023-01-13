import random
def prRed(skk): print("\033[31m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[32m {}\033[00m" .format(skk))
def prBlue(skk): print("\033[34m {}\033[00m" .format(skk))

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
game_continue = ""

while True:
    player_move = input("Choose[r]ock, [p]aper or [s]cissors :")
    
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Please try again...")
        
    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    
    prBlue(f"The computer chose {computer_move}.")
        
    if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
        prGreen("You win!")
        game_continue = input("Type [yes] to play again or [no] to quit.")
        if game_continue == "yes":
            continue
        else:
            print("Thank you for playing.")
            break
    elif player_move == computer_move:
        prYellow("Draw!")
        game_continue = input("Type [yes] to play again or [no] to quit.")
        if game_continue == "yes":
            continue
        else:
            print("Thank you for playing.")
            break
    else:
        prRed("You lose!")
        game_continue = input("Type [yes] to play again or [no] to quit.")
        if game_continue == "yes":
            continue
        else:
            print("Thank you for playing.")
            break
