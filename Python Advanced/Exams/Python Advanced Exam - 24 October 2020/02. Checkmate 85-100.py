board, result = [], []

for row in range(8):
    board.append(input().split())
    for col in range(8):
        if board[row][col] == "K":
            king = [row, col]

def row_check(king_row, end, step):
    for row in range(king_row, end, step):
        if board[row][king[1]] == "Q":
            return [row, king[1]]
            
def col_check(king_col, end, step):
    for col in range(king_col, end, step):
        if board[king[0]][col] == "Q":
            return [king[0], col]

def diag_check(row_start, row_end, col_start, col_end):
    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            if board[row][col] == "Q":
                if row_start == 0 and king[0] != 0:
                    if col_start == 0 and king[1] != 0:
                        if row_end - row == col_end - col:
                            return [row, col]
                    else:
                        if row_end - row ==  col - col_start:
                            return [row, col]
                else:
                    if col_start == 0 and king[1] != 0:
                        if row - row_start == col_end - col:
                            return [row, col]
                    else:
                        if row - row_start ==  col - col_start:
                            return [row, col]
                        
#checking up, down, left and right
result.append(row_check(king[0], 8, 1))
result.append(row_check(king[0] - 1, -1, -1))
result.append(col_check(king[1], 8, 1))
result.append(col_check(king[1] - 1, -1, -1))
#checking the four directions of diagonals
result.append(diag_check(0, king[0], 0, king[1]))
result.append(diag_check(king[0], 8, king[1], 8))
result.append(diag_check(0, king[0], king[1], 8))
result.append(diag_check(king[0], 8, 0, king[1]))


if result == 8 * [None]:
    print("The king is safe!")
else:
    for r in result:
        if r != None:
            print(r)
