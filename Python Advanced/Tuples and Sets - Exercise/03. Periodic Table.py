inputs = int(input())
all_elements = []
for i in range(inputs):
    all_elements += input().split()
print(*set(all_elements), sep="\n")

# elements - set()
# for i in range(int(input())):
#     for el in input().split():
#         table.add(el)
# print(*table, sep="\n")
