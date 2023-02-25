command = input()
products = {}
while command != "statistics":
    command = command.split(": ")
    key = command[0]
    value = int(command[1])
    if key not in products:
        products[key] = 0
    products[key] += value
    command = input()
    
result = "Products in stock:\n"
for (key, value) in products.items():
    result += f"- {key}: {value}\n"
result += f"Total Products: {len(products.keys())}\n"
result += f"Total Quantity: {sum(products.values())}"
print(result)
