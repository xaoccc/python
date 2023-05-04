class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        result = 0
        for i in range(len(grid)):
            
            for j in range(len(grid[i])):
                max_current_height = [max(grid[i])]
                for k in range(len(grid[i])):
                    max_current_height.append(grid[k][j])
                max_possible_height = min([max_current_height[0], max(max_current_height[1:])])
                height_to_add = max_possible_height - max_current_height[i+1]
                if height_to_add < 0:
                    height_to_add = 0

                result += height_to_add
        return result
