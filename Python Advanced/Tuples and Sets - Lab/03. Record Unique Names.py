names_num = int(input())
names = []

for i in range(names_num):
    names.append(input())
print(*set(names), sep="\n")
