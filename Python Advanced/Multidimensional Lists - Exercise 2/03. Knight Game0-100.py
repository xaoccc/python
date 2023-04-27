board_size = int(input())
board = [list(input()) for i in range(board_size)]
attacks = {}
can_attack = True
knights_removed = 0

while can_attack:
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == "K":
                if row - 2 >= 0:
                    if col - 1 >= 0:
                        if board[row - 2][col - 1] == "K":
                            if (row - 2, col - 1) not in attacks:
                                attacks[(row - 2, col - 1)] = 1
                            else:
                                attacks[(row - 2, col - 1)] += 1
                    elif col + 1 < board_size:
                        if board[row - 2][col + 1] == "K":
                            if (row - 2, col + 1) not in attacks:
                                attacks[(row - 2, col + 1)] = 1
                            else:
                                attacks[(row - 2, col + 1)] += 1
                
                elif row - 1 >= 0:
                    if col - 2 >= 0:
                        if board[row - 1][col - 2] == "K":
                            if (row - 1, col - 2) not in attacks:
                                attacks[(row - 1, col - 2)] = 1
                            else:
                                attacks[(row - 1, col - 2)] += 1
                    elif col + 2 < board_size:
                        if board[row - 1][col + 2] == "K":
                            if (row - 1, col + 2) not in attacks:
                                attacks[(row - 1, col + 2)] = 1
                            else:
                                attacks[(row - 1, col + 2)] += 1
                                
                if col - 2 >= 0:
                    if row - 1 >= 0:
                        if board[row - 1][col - 2] == "K":
                            if (row - 1, col - 2) not in attacks:
                                attacks[(row - 1, col - 2)] = 1
                            else:
                                attacks[(row - 1, col - 2)] += 1
                    elif row + 1 < board_size:
                        if board[row + 1][col - 2] == "K":
                            if (row + 1, col - 2) not in attacks:
                                attacks[(row + 1, col - 2)] = 1
                            else:
                                attacks[(row + 1, col - 2)] += 1
                
                elif col - 1 >= 0:
                    if row - 2 >= 0:
                        if board[row - 2][col - 1] == "K":
                            if (row - 2, col - 1) not in attacks:
                                attacks[(row - 2, col - 1)] = 1
                            else:
                                attacks[(row - 2, col - 1)] += 1
                    elif row + 2 < board_size:
                        if board[row + 2][col - 1] == "K":
                            if (row + 2, col - 1) not in attacks:
                                attacks[(row + 2, col - 1)] = 1
                            else:
                                attacks[(row + 2, col - 1)] += 1
    attacks = dict(sorted(attacks.items(), key=lambda x: (-x[1], sum(x[0]))))
    if len(attacks) == 0:
        can_attack = False
    else:
        first_key = next(iter(attacks))
        board[first_key[0]][first_key[1]] = "0"
        knights_removed += 1
        attacks = {}
        
print(knights_removed)
