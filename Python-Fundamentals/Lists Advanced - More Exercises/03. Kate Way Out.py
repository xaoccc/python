rows = int(input())
# Let us divide the problem into several small poblems
# 1. We need a map of the maze and a place to store all possible solutions
maze, solutions = [], []
# 2. We have to find out where is the starting point of Kate and the size of the maze (start_row, start_column, columns, rows)
start_row, start_column, columns = 0, 0, 0
for i in range(rows):
    current_row = input()
    columns = len(current_row)
    maze.append(list(current_row))
    if "k" in current_row:
        start_row = i
        start_column = current_row.index("k")

# 3. We create a funcion to find each possible path and using recursion and backtracking, store it in the list solutions. We may do it in several ways - 
# by counting the steps and adding total number of each step into the solutions list or record each step coordinates and again put them in the list.
# I used the second type of solution, which can be used also to trace and draw if you like each possible path. 
def find_path(row, col, maze, path):
    
    # 4. In the function, we define the conditions by which we have a finished path and this finished path is being added to the solutions list.
    if row == rows or row == -1 or col == columns or col == -1:
        solutions.append(len(path))
        return
    # 5. Here is the base condition (terminating condition). In this case we check if Kate reaches the end of the maze, visited cell or a wall
    if 0 > row >= rows or 0 > col >= columns or maze[row][col] == "visited" or maze[row][col] == "#":
        return

    # 6. If the current row and column are valid, Kate moves 1 step and we add the coordinates (row, col) to the current path.
    path.append([row, col])
    # 7. We also mark this cell with coordinates (row, col) as visited
    maze[row][col] = "visited"

    # 8. We check all neighbouring cells for a valid cell, so Kate may continue her way in the maze:
    # The cel below
    find_path(row - 1, col, maze, path)
    # The cell above
    find_path(row + 1, col, maze, path)
    # The cell on the left
    find_path(row, col - 1, maze, path)
    # The cell on the right
    find_path(row, col + 1, maze, path)
    # 9. Here is the backtracking. Since none of the solutions (above, below, left, right) worked in the check for valid neighbouring cell,
    # We should return 1 step back for a new solution, so we unmark the current cell as visited and remove the coordinates from the path.
    maze[row][col] = " "
    path.pop()

find_path(start_row, start_column, maze, [])

# 10. The output. Here we have finished checking for all possible valid paths (if any)
# If there are no such, Kate cannot get out of the maze, if there are such paths, we find the longest and print the result.
# Note that we can easily change the output and check for shortest or average path, or print the actual path by directions or coordinates 
# By configuring line 22 to add not the length, but the actual path, we may easily change the output, so this may be a general solution for this type of problems.
if len(solutions) == 0:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {max(solutions)} moves")
