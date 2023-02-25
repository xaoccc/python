resource = input()
dictionary = {}
while resource != "stop":
    qty = int(input())
    if resource not in dictionary:
        dictionary[resource] = 0
    dictionary[resource] += qty
    resource = input()
for (key, value) in dictionary.items():
    print(f"{key} -> {value}")
