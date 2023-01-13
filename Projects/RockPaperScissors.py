import random
from colorama import Fore, Back, Style

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
    
    print(Fore.BLUE + f"The computer chose {computer_move}.")
        
    if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
        print(Fore.GREEN +"You win!")
        game_continue = input("Type [yes] to play again or [no] to quit.")
        if game_continue == "yes":
            continue
        else:
            print("Thank you for playing")
            break
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
        game_continue = input("Type [yes] to play again or [no] to quit.")
        if game_continue == "yes":
            continue
        else:
            print("Thank you for playing")
            break
    else:
        print(Fore.RED + "You lose!")
        game_continue = input("Type [yes] to play again or [no] to quit.")
        if game_continue == "yes":
            continue
        else:
            print("Thank you for playing")
            break
