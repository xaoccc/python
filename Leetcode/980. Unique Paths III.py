legit_path_len = len(grid) * len(grid[0])

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 1:
            start_row = row
            start_column = col
        if grid[row][col] == -1:
            legit_path_len -= 1
         
rows, cols = len(grid), len(grid[0])


def find_path(row, col, path, solutions):


    if 0 > row  or row == rows or 0 > col or col == cols :
        return 
    
    if grid[row][col] == "visited" or grid[row][col] == -1:
        return 
    
    if grid[row][col] == 2:
        if len(path) == legit_path_len - 1:
            solutions.append(path.copy())
            solutions[-1].append((row, col))
        return 


    path.append((row, col))
    grid[row][col] = "visited"

    find_path(row - 1, col, path, solutions)
    find_path(row + 1, col, path, solutions)
    find_path(row, col - 1, path, solutions)
    find_path(row, col + 1, path, solutions)

    grid[row][col] = " "
    path.pop()
    
    

solutions = []
find_path(start_row, start_column, [], solutions)


result = ""
for i in range(1, len(solutions) + 1):
    result += f"{i}. {solutions[i-1]}\n"



print(result)
