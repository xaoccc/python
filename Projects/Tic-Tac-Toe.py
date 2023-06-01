player_one, player_two = None, None
board = [["", "", ""], ["", "", ""], ["", "", ""]]
setup()
current = player_one
other = player_two
loop = True

while loop:
    play(current, board)
    current, other = other, current

def setup():
    global player_one, player_two
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    player_one_sign = input(f"{player_one_name}, please choose a sign (X or O):" )
    player_two_sign = "X" if player_one_sign == "O" else "O"
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print(f"This is the numeration of the board:\n{' '.join(['| ' + str(i) for i in range(1,4)])} |\n{' '.join(['| ' + str(i) for i in range(4,7)])} |\n{' '.join(['| ' + str(i) for i in range(7,10)])} |\n{player_one_name} starts first!")
    

def play(current, board):
    choice = int(input(f"{current[0]} Chooce a free position [0-9]: "))
    row = ceil(choice / 3) - 1
    col = choice % 3 - 1
    draw_board(board)
    check_if_won(current, board)
