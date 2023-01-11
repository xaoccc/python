quantity = int(input())
days_left = int(input())
purchase_cost = 0
spirit = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        purchase_cost += quantity * 2
        spirit += 5
    if day % 3 == 0:
        purchase_cost += quantity * 8
        spirit += 13
    if day % 5 == 0:
        purchase_cost += quantity * 15
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        purchase_cost += 23
        if day == days_left:
            spirit -= 30
            
print(f"Total cost: {purchase_cost}")
print(f"Total spirit: {spirit}")
