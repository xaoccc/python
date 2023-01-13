import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose[r]ock, [p]aper or [s]cissors :")

if player_move = "r":
    player_move = rock
elif player_move = "p":
    player_move = paper
elif player_move = "s":
    player_move = scissors
else:
    raise SystemExit("Invalid input. Please try again...")
    
computer_move = random.randint(1, 3)
