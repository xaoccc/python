from math import ceil
player_one, player_two = None, None
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def setup():
    global player_one, player_two
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    player_one_sign = input(f"{player_one_name}, please choose a sign (X or O):" )
    player_two_sign = "X" if player_one_sign == "O" else "O"
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print(f"This is the numeration of the board:\n{' '.join(['| ' + str(i) for i in range(1,4)])} |\n{' '.join(['| ' + str(i) for i in range(4,7)])} |\n{' '.join(['| ' + str(i) for i in range(7,10)])} |\n{player_one_name} starts first!")
    
    
def draw_board(board):
    for row in board:
        print("| ", end="")
        print(" | ".join([str(x) for x in row]), end="")
        print(" |")
    
    
def check_if_won(current, board):
    global loop
    first_row = all([x == current[1] for x in board[0]])
    second_row = all([x == current[1] for x in board[1]])
    third_row = all([x == current[1] for x in board[2]])
    first_column = all([x == current[1] for x in [board[0][0], board[1][0], board[2][0]]])
    second_column = all([x == current[1] for x in [board[0][1], board[1][1], board[2][1]]])
    third_column = all([x == current[1] for x in [board[0][2], board[1][2], board[2][2]]])
    first_diagonal = all([x == current[1] for x in [board[0][0], board[1][1], board[2][2]]])
    second_diagonal = all([x == current[1] for x in [board[2][0], board[1][1], board[0][2]]])
    if any ([first_row, second_row, third_row, first_column, second_column, third_column, first_diagonal, second_diagonal]):
        print(f"Player {current[0]} has won!")
        loop = False
        
        
def play(current, board):
    choice = int(input(f"{current[0]}, choose a free position [0-9]: "))
    if choice < 1 or choice > 9:
        while 1 > choice or choice > 9:
            choice = int(input(f"Invalid choice. {current[0]}, choose a VALID free position [0-9]: "))
            
    row = ceil(choice / 3) - 1
    col = choice % 3 - 1
    if board[row][col] == "X" or board[row][col] == "O":
        while board[row][col] == "X" or board[row][col] == "O":
            choice = int(input(f"Invalid choice. {current[0]}, choose a FREE position [0-9]: "))
            if choice < 1 or choice > 9:
                while 1 > choice or choice > 9:
                    choice = int(input(f"Invalid choice. {current[0]}, choose a VALID free position [0-9]: "))
            row = ceil(choice / 3) - 1
            col = choice % 3 - 1
    
    board[row][col] = current[1]
    draw_board(board)
    check_if_won(current, board)
   
        
setup()
current = player_one
other = player_two
loop = True

while loop:
    play(current, board)
    current, other = other, current
