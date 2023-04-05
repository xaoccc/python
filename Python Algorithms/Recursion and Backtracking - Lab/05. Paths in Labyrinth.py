rows = int(input())
columns = int(input())
labir = []
for i in range(rows):
    labir.append(list(input()))

def find_path(row, col, labir, direct, path):
    if rows <= row < 0 or columns <= col < 0 :
        return
    
    if labir[row][col] == "*":
        return
    
    if labir[row][col] == "visited":
        return
    
    path.append(direct)
    
    if labir[row][col] == "e":
        print("".join(path))
        path.pop()
        
    else:
        labir[row][col] == "visited"
        
        find_path(row - 1, col, labir, "U", path)
        find_path(row + 1, col, labir, "D", path)
        find_path(row, col - 1, labir, "L", path)
        find_path(row, col + 1, labir, "R", path)
        #mark current cell as free for further use for another possible path:
        labir[row][col] == "-"
        
    #remove the last visited cell
    path.pop()
        

find_path(0, 0, labir, '', [])
