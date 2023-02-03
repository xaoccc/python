board = input().split()
command = input()
moves_num = 0

while command != "end":
    current_command = [int(i) for i in command.split()]
    moves_num += 1
    
    if current_command[0] < 0 or current_command[0] >= len(board) or current_command[1] < 0 or current_command[1] >= len(board) or current_command[0] == current_command[1]:
        print("Invalid input! Adding additional elements to the board")
        board.insert(len(board)//2, "-" + str(moves_num) + "a")
        board.insert(len(board)//2, "-" + str(moves_num) + "a")
    elif board[int(current_command[0])] != board[int(current_command[1])]:
        print("Try again!")
    else:
        print(f"Congrats! You have found matching elements - {board[current_command[0]]}!")
        if current_command[1] > current_command[0]:
            del [board[current_command[1]], board[current_command[0]]]
        else:
            del [board[current_command[0]], board[current_command[1]]]
            
    if len(board) == 0:
        print(f"You have won in {moves_num} turns!")
        break
    command = input()
    
if len(board) > 0:
    print("Sorry you lose :(")
    print(" ".join(board))
