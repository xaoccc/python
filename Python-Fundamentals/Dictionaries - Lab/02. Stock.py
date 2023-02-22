elements = input().split()
needed = input().split()
products = {}
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    products[key] = int(value)

for i in needed:
    if i in products:
        print(f"We have {products[i]} of {i} left")
    else:
        print(f"Sorry, we don't have {i}")
