class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left = []
        right = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i == j:
                    left.append(mat[i][j])
                if i + j == len(mat) - 1:
                    right.append(mat[i][j])
        if len(mat) % 2 == 0:
            return sum(left) + sum(right)
        else:
            return sum(left) + sum(right) - mat[len(mat)//2][len(mat)//2]
