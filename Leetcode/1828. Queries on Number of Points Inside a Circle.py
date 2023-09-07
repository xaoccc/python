class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = [0] * len(queries)

        for i in range(len(queries)):            
            current_radius = queries[i][2]
            for p in points:                
                distance = math.sqrt((p[0] - queries[i][0])**2 + (p[1] - queries[i][1])**2)
                if current_radius >= distance:
                    result[i] += 1
        return result
