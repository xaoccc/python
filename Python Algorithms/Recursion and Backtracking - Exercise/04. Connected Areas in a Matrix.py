

def find_area(row, col, matrix):
    if row >= rows or col >= cols or row < 0 or col < 0:
        return 0

    if matrix[row][col] != "-":
        return 0

    matrix[row][col] = "v"
    area = 1
    area += find_area(row + 1, col, matrix)
    area += find_area(row - 1, col, matrix)
    area += find_area(row, col + 1, matrix)
    area += find_area(row, col - 1, matrix)
    return area

rows = int(input())
cols = int(input())
matrix = []

for i in range(rows):
    matrix.append(list(input()))
total_areas = 0
res = []
for row in range(rows):
    for col in range(cols):
        area = find_area(row, col, matrix)
        if area > 0:
            total_areas += 1
            res.append(f"Area #{total_areas} at ({row}, {col}), size: {area}")
print(total_areas)
print(f"Total areas found: {total_areas}")
for i in range(total_areas):
    print(res[i])