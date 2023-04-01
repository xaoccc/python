lists = input().split("|")
result = []
final = []
for current in lists:
    current = current.strip(" ").split()
    result.insert(0, current)
for i in result:
    final += i
print(*final)