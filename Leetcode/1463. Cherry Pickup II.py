class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        from functools import lru_cache
        
        rows, cols = len(grid), len(grid[0])

        @lru_cache(None)
        def cherries(row, col1, col2):

            
            if row == rows or col1 < 0 or col2 < 0 or col1 >= cols or col2 >= cols:
                return 0
            
            cherries_count = grid[row][col1]
            if col1 != col2:
                cherries_count += grid[row][col2]
            
            temp_res = 0
            for i in range(col1 - 1, col1 + 2):
                for j in range(col2 - 1, col2 + 2):
                    temp_res = max(temp_res, cherries(row + 1, i, j))
            

            return cherries_count + temp_res 

            
        return cherries(0, 0, cols-1)
