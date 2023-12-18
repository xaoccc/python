class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])

        for i in range(max([rows, cols])):
            for row in range(0, rows - 1):
                for col in range(0, cols - 1):
                    if mat[row][col] > mat[row + 1][col + 1]:
                        mat[row][col], mat[row + 1][col + 1] = mat[row + 1][col + 1], mat[row][col]


        return mat