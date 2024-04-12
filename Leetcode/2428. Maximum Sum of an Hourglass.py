class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 3 and len(grid[0]) == 3:
            return sum(grid[0]) + grid[1][1] + sum(grid[2])

        else:
            grid_sums = []
            for i in range(0, len(grid) - 2):
                for j in range(0, len(grid[0]) - 2):
                    current_sum = sum(grid[i][j: j+3]) + grid[i + 1][j+1] + sum(grid[i + 2][j: j+3])
                    grid_sums.append(current_sum)
            return max(grid_sums)