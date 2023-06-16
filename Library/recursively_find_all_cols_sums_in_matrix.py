def cols_sum(j, grid, result):
   if j >= cols:
      return result
   s = sum([grid[i][j] for i in range(rows)])
   result.append(s)
   return cols_sum(j + 1, grid, result)

# j - starting col
# grid == matrix
# result - a list with the sum of each column
