board = input().split()
command = input()
moves_num = 0

while command == "end":
    current_command = command.split()
    moves_num += 1
        if board[int(current_command[0])] != board[int(current_command[1])]:
            print("Try again!")
        elif int(current_command[0]) < 0 or int(current_command[0]) >= len(board) or int(current_command[1]) < 0 or int(current_command[1]) >= len(board) or int(current_command[0]) == int(current_command[1]):
            print("Invalid input! Adding additional elements to the board")
            board.insert(len(board)//2, "-" + str(moves_num) + "a")
