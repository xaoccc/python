rows = int(input())
columns = int(input())
labir = []
for i in range(rows):
    labir.append(list(input()))


def find_path(row, col, labir, direct, path):
    if rows <= row or row < 0 or columns <= col or col < 0:
        return
    
    if labir[row][col] == "*":
        return
    
    if labir[row][col] == "visited":
        return
    path.append(direct)

    if labir[row][col] == "e":
        print("".join(path))

    else:
        labir[row][col] = "visited"

        find_path(row - 1, col, labir, "U", path)
        find_path(row + 1, col, labir, "D", path)
        find_path(row, col - 1, labir, "L", path)
        find_path(row, col + 1, labir, "R", path)
        labir[row][col] = "-"

    path.pop()
        

find_path(0, 0, labir, '', [])
