rows = int(input())
sum = 0
for i in range(rows):
    sum += [int(i) for i in input().split()][i]
print(sum)

# def primary_dialonal_sum(rows, total):
#     for i in range(rows):
#         total += [int(i) for i in input().split()][i]
#     return total
# print(primary_dialonal_sum(int(input()), 0))
