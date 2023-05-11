board_size = int(input())
board = [list(input()) for i in range(board_size)]
knights_removed = 0
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
                if row - 2 >= 0:
                    # Check 1: row - 2, col - 1
                    if col - 1 >= 0:
                        if board[row - 2][col - 1] == "K":
                            count_attaks(attacks, row, col)
                    # Check 1: row - 2, col + 1
                    if col + 1 < board_size:
                        if board[row - 2][col + 1] == "K":
                            count_attaks(attacks, row, col)                            
                if row - 1 >= 0:
                    # Check 3: row - 1, col - 2
                    if col - 2 >= 0:
                        if board[row - 1][col - 2] == "K":
                            count_attaks(attacks, row, col)
                    # Check 4: row - 1, col + 2
                    if col + 2 < board_size:
                        if board[row - 1][col + 2] == "K":
                            count_attaks(attacks, row, col)
                if col - 2 >= 0:
                    # Check 5: row + 1, col - 2
                    if row + 1 < board_size:
                        if board[row + 1][col - 2] == "K":
                            count_attaks(attacks, row, col)                            
                if row + 2 < board_size:
                    # Check 6: row + 2, col + 1
                    if col + 1 < board_size:
                        if board[row + 2][col + 1] == "K":
                            count_attaks(attacks, row, col)
                    # Check 7: row + 2, col + 1
                    if col - 1 >= 0:
                        if board[row + 2][col - 1] == "K":
                            count_attaks(attacks, row, col)                            
                if row + 1 < board_size:
                    # Check 8: row + 1, col + 2
                    if col + 2 < board_size:
                        if board[row + 1][col + 2] == "K":
                            count_attaks(attacks, row, col)
                            
    # -x[1] is sorting by the coordinates of the knight who can attack the greatest number of knights. No other sorting is needed.
    attacks = dict(sorted(attacks.items(), key=lambda x: (-x[1])))
    # If no knight can attack, we exit the loop
    if len(attacks) == 0:
        break
    else:
        # Get the coordinates of the knight to be removed and remove him by replacing "K" with "0"
        first_key = next(iter(attacks))
        board[first_key[0]][first_key[1]] = "0"
        # Add removed knight to the total number of removed knights
        knights_removed += 1
        
print(knights_removed)
