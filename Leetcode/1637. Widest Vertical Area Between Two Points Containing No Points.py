class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = list(sorted(points))
        max_width = 0
        for i in range(1, len(points)):
            if points[i][0] - points[i - 1][0] > max_width:
                max_width = points[i][0] - points[i - 1][0]

        return max_width
