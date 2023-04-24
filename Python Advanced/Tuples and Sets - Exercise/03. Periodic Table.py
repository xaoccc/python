inputs = int(input())
all_elements = []
for i in range(inputs):
    all_elements += input().split()
print(*set(all_elements), sep="\n")
