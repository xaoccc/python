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

def up_left_diag_check():
    for row in range(0, king[0]):
        for col in range(0, king[1]):
            if board[row][col] == "Q" and king[0] - row == king[1] - col:
                return [row, col]
                
def up_left_diag_check():
    for row in range(0, king[0]):
        for col in range(0, king[1]):
            if board[row][col] == "Q" and king[0] - row == king[1] - col:
                return [row, col]                
                
def down_right_diag_check():   
    for row in range(king[0], 8):
        for col in range(king[1], 8):
            if board[row][col] == "Q" and row - king[0] == col - king[1]:
                return [row, col] 
                
def up_right_diag_check():
    for row in range(0, king[0]):
        for col in range(king[1], 8):
            if board[row][col] == "Q" and king[0] - row == col - king[1]:
                return [row, col]  
                
def down_left_diag_check():
    for row in range(king[0], 8):
        for col in range(0, king[1]):
            if board[row][col] == "Q" and row - king[0] == king[1] - col:
                return [row, col]
        
result.append(row_check(king[0], 8, 1))
result.append(row_check(king[0] - 1, -1, -1))
result.append(col_check(king[1], 8, 1))
result.append(col_check(king[1] - 1, -1, -1))
result.append(up_left_diag_check())
result.append(down_right_diag_check())
result.append(up_right_diag_check())
result.append(down_left_diag_check())

if result == 8 * [None]:
    print("The king is safe!")
else:
    for r in result:
        if r != None:
            print(r)
