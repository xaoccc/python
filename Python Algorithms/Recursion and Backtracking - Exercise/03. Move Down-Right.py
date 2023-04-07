def unique_paths(row, col, rows, cols):
    if row == rows or col == cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += unique_paths(row + 1, col, rows, cols)
    result += unique_paths(row, col + 1, rows, cols)
    return result


rows = int(input())
cols = int(input())


print(unique_paths(0, 0, rows, cols))