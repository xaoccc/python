import random
def prRed(skk): print("\033[31m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[32m {}\033[00m" .format(skk))
def prBlue(skk): print("\033[34m {}\033[00m" .format(skk))


computer_number = random.randint(1, 100)
tries_num = 0

while True:
    player_input = int(input("Guess the number (1-100): "))
    if 1 > player_input > 100:
        prRed("Invalid input! Try again.")
        continue
    elif player_input > computer_number:
        prRed("Too high!")
        tries_num += 1
    elif player_input < computer_number:
        prRed("Too low!")
        tries_num += 1
    else:
        prBlue(f"You guessed it with {tries_num} attempts")
        break
