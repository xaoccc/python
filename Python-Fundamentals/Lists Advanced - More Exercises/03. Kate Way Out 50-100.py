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
    def find_path(row, col, maze, path):

        if row < rows and col < columns and row > -1 and columns > -1:
            if maze[row][col] == "visited":
                return
        if row < rows and col < columns and row > -1 and columns > -1:
            if maze[row][col] == "#":
                return
        if row == rows or row == -1 or col == columns or col == -1:
            #debug code solutions.append(path)
            solutions.append(len(path))
            return
    
        maze[row][col] = "visited"
        path.append([row, col])
    
        find_path(row - 1, col, maze, path)
        find_path(row + 1, col, maze, path)
        find_path(row, col - 1, maze, path)
        find_path(row, col + 1, maze, path)
    
        maze[row][col] = " "
    
    find_path(start_row, start_column, maze, [])
    
    if len(solutions) == 0:
        print("Kate cannot get out")
    else:
        # debug code print(solutions)
        print(f"Kate got out in {max(solutions)} moves")
