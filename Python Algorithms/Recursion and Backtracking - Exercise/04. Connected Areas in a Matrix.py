

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
result = []
for row in range(rows):
    for col in range(cols):
        area = find_area(row, col, matrix)
        if area > 0:
            total_areas += 1
            result.append([row, col, area])
result.sort(key=lambda x: x[2], reverse=True)
print(f"Total areas found: {total_areas}")
for i in range(total_areas):
    print(f"Area #{i + 1} at ({result[i][0]}, {result[i][1]}), size: {result[i][2]}")