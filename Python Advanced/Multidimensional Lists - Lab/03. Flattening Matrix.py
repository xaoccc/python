inputs_num = int(input())
result = []
for i in range(inputs_num):
    result += [int(j) for j in input().split(", ")]
print(result)
