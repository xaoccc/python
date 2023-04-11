def find_max_dots(row, col, chars_map):
    if 0 > row or row >= rows or 0 > col or col >= cols:
        return 0
    if chars_map[row][col] == "-" or chars_map[row][col] == "v":
        return 0
    
    chars_map[row][col] = "v"
    area = 1
    area += find_max_dots(row - 1, col, chars_map)
    area += find_max_dots(row + 1, col, chars_map)
    area += find_max_dots(row, col - 1, chars_map)
    area += find_max_dots(row, col + 1, chars_map)
    return area
 
rows = int(input())
chars_map, result = [], []

for i in range(rows):
    row = input()
    chars_map.append(row.split())
cols = len(chars_map[0])

for row in range(rows):
    for col in range(cols):
        area = find_max_dots(row, col, chars_map)
        result.append(area)
print(max(result))
