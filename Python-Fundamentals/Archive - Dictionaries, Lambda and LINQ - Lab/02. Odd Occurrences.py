text = [i.lower() for i in input().split()]
result = []
for i in text:
    if text.count(i) % 2 != 0 and i not in result:
        result.append(i)
print(*result, sep=", ")
