def unique_paths(row, col, rows, cols):
    #if we hit cell outside the map, we have no valid path, so return 0 (No path to count)
    if row == rows or col == cols:
        return 0

    # Every time when in unique_paths(row + 1, col, rows, cols) or unique_paths(row, col + 1, rows, cols)
    # row == rows - 1 and col == cols - 1, the result is 1
    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    # We add each result(return) of the nested function to the total result
    result += unique_paths(row + 1, col, rows, cols)
    result += unique_paths(row, col + 1, rows, cols)
    # Here is the place for the result
    return result


rows = int(input())
cols = int(input())


print(unique_paths(0, 0, rows, cols))