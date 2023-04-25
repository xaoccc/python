rows = int(input())
sum = 0
for i in range(rows):
    sum += [int(i) for i in input().split()][i]
print(sum)
