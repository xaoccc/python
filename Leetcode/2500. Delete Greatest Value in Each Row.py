class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        i = 0
        result = 0
        max_num = 0
        while True:
            result += max_num
            if len(grid[i]) == 0:
                break
            max_num = 0
            for i in range(len(grid)):
                if max_num < max(grid[i]):
                    max_num = max(grid[i])
                grid[i].remove(max(grid[i]))
        return result
