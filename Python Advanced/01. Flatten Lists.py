matrix = [i.split() for i in input().split("|")]
matrix.reverse()
print(*(' '.join(i) for i in matrix))
