class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        def cols_sum(j, grid, result):
            if j >= cols:
                return result
            s = sum([grid[i][j] for i in range(rows)])
            result.append(s)
            return cols_sum(j + 1, grid, result)


        diff = []
        cols = len(grid[0])
        rows = len(grid)
        sum_cols = cols_sum(0, grid, [])

        for i in range(rows):
            diff.append([])
            ones_row_sum = sum(grid[i])
            zeros_row_sum = cols - ones_row_sum
            for j in range(cols):
                diff[i].append(ones_row_sum + sum_cols[j] - zeros_row_sum - (rows - sum_cols[j]))

        return diff
