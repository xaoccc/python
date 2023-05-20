board_size = int(input())
board = [list(input()) for i in range(board_size)]
knights_removed = 0
a = [-2, -1, 1, 2]
moves = [(x, y) for x in a for y in a if abs(x) != abs(y)]

def count_attaks(attacks, row, col):
    if (row, col) not in attacks:
        attacks[(row, col)] = 1
    else:
        attacks[(row, col)] += 1
    return attacks

while True:
    attacks = {}
    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == "K":
                for move in moves:
                    if -1 < row + move[0] < board_size and -1 < col + move[1] < board_size and board[row + move[0]][col + move[1]] == "K":
                        count_attaks(attacks, row, col)

    attacks = dict(sorted(attacks.items(), key=lambda x: (-x[1])))
    if len(attacks) == 0:
        break
    else:
        first_key = next(iter(attacks))
        board[first_key[0]][first_key[1]] = "0"
        knights_removed += 1
        
print(knights_removed)
