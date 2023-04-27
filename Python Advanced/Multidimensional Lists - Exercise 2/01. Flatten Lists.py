matrix = [i.split() for i in input().split("|")[::-1]]
for i in matrix:
    for j in i:
        print(j, end=" ")
