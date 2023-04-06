rows = int(input())
maze, solutions = [], []
for i in range(rows):
    current_row = input()
    columns = len(current_row)
    maze.append(list(current_row))
    if "k" in current_row:
        start_row = i
        start_column = current_row.index("k")
     
if start_row == 0 or start_row == rows - 1 or start_column == 0 or start_column == columns - 1:
    print(f"Kate got out in 1 moves")

else:
    def find_path(row, col, maze, direct, path):
    
        if row < rows and col < columns and row > -1 and columns > -1:
            if maze[row][col] == "visited":
                return
        if row < rows and col < columns and row > -1 and columns > -1:
            if maze[row][col] == "#":
                return
        if rows == row or row == 0 or columns == col or col == 0:
            solutions.append(len(path))
            return
    
        maze[row][col] = "visited"
        path.append(direct)
    
        find_path(row - 1, col, maze, "U", path)
        find_path(row + 1, col, maze, "D", path)
        find_path(row, col - 1, maze, "L", path)
        find_path(row, col + 1, maze, "R", path)
    
        maze[row][col] = " "
    
    find_path(start_row, start_column, maze, '', [])
    
    if len(solutions) == 0:
        print("Kate cannot get out")
    else:
        print(f"Kate got out in {min(solutions)} moves")
