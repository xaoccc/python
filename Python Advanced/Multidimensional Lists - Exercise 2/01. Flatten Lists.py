matrix = [i.split() for i in input().split("|")[::-1]]
print(*(' '.join(i) for i in matrix if i))
