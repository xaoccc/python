class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = []
        result = 0
        for i in range(m):
            matrix.append([])
            for j in range(n):
                matrix[i].append(0)
        for j in range(len(indices)): 
            for i in range(n):
                matrix[indices[j][0]][i] += 1
            for i in range(m):
                matrix[i][indices[j][1]] += 1

        for row in range(m):
            for col in range(n):
                if matrix[row][col] % 2 != 0:
                    result += 1
        return result
