rows = int(input())
columns = int(input())
#create a labirinth with all the data
labir = []
for i in range(rows):
    labir.append(list(input()))

# Our function should contain the current current row number, column number, the labirinth itself, the direction and a
# place to store each valid path


def find_path(row, col, labir, direct, path):
    # if current column number or current row number is outside of labirinth, do not execute the code(return)
    if rows <= row or row < 0 or columns <= col or col < 0:
        return
    # if there is an obstacle(*), do not execute the code(return)
    if labir[row][col] == "*":
        return
    # if the cell is marked as visited, do not execute the code(return)
    if labir[row][col] == "visited":
        return
    # if none of the above happen, add direction to the path list
    path.append(direct)

    # if current cell is "e", this means we exit the labirinth and we should print an output
    if labir[row][col] == "e":
        print("".join(path))

    # The magic happens here. If
    # 1. We are in the labirinth
    # 2. Current cell is not * or e or visited
    # This means we are on valid unvisited cell and we start/continue our way to the exit
    else:
        # First we mark the cell as visited
        labir[row][col] = "visited"

        # then we choose a direction. For example, if all directions are valid, we go up (direct=="U"),
        # if our previous row was 3, now it becomes  3-1=2 and the column number remains the same
        # If it was visited or invalid, we would check next one (down), and next one(left) or next one(right)
        # until we find a valid one.
        # If there is no valid direction and we have no way out(finished path), the program exits without printing result
        find_path(row - 1, col, labir, "U", path)
        find_path(row + 1, col, labir, "D", path)
        find_path(row, col - 1, labir, "L", path)
        find_path(row, col + 1, labir, "R", path)
        # When a path is found or not but we tried a route, we must unmark the visited cell again as valid
        # if we are here the cell cannot be "e" or "*"
        labir[row][col] = "-"

    # remove the last element from the path
    path.pop()
        
# the initial data for our function - we start with column 0, row 0, the labirinth from the problem condition,
# empty string for the directions and empty list for the path
find_path(0, 0, labir, '', [])
