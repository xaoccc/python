def get_magic_triangle(n):
    matrix = [[1]]
    for i in range(1, n):
        matrix.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                matrix[i].append(matrix[i-1][0])
            else:
                matrix[i].append(matrix[i-1][j-1] + matrix[i-1][j])
    return matrix
