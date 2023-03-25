command = input()
stock = {}
grand_total = 0
while command != "stocked":
    command = command.split()
    if command[0] not in stock.keys():
        stock[command[0]] = [float(command[1]), int(command[2])]
    else:
        stock[command[0]][0] = float(command[1])
        stock[command[0]][1] += int(command[2])
    command = input()
    
for item, item_data in stock.items():
    total = item_data[0] * item_data[1]
    grand_total += total
    print(f"{item}: ${item_data[0]:.2f} * {item_data[1]} = ${total:.2f}")
    
print(f"{'-'*30}\nGrand Total: ${grand_total:.2f}")
