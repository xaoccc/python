def mark_red(matrix, row, col):
    
    if row < 0 or row > rows or col < 0 or col > cols:
        return
    
    if matrix[row][col] != "current_box_color":
        return
    
    if matrix[row][col] == "current_box_color":
        matrix[row][col] = "red"

    mark(matrix, row - 1, col)
    mark(matrix, row, col - 1)
    mark(matrix, row + 1, col)
    mark(matrix, row, col + 1)
    
    return matrix
