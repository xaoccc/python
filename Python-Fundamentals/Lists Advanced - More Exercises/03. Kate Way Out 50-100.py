rows = int(input())
maze, solutions = [], []
start_row, start_column, columns = 0, 0, 0
for i in range(rows):
    current_row = input()
    columns = len(current_row)
    maze.append(list(current_row))
    if "k" in current_row:
        start_row = i
        start_column = current_row.index("k")

     
def find_path(row, col, maze, path):

    if row == rows or row == -1 or col == columns or col == -1:
        solutions.append(len(path))
        return

    if 0 > row >= rows or 0 > col >= columns or maze[row][col] == "visited" or maze[row][col] == "#":
        return

    path.append([row, col])
    maze[row][col] = "visited"


    find_path(row - 1, col, maze, path)
    find_path(row + 1, col, maze, path)
    find_path(row, col - 1, maze, path)
    find_path(row, col + 1, maze, path)
    maze[row][col] = " "
    path.pop()

find_path(start_row, start_column, maze, [])

if len(solutions) == 0:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {max(solutions)} moves")
