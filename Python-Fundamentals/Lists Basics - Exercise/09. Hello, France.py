items_list = input()
budget = float(input())
items_list = items_list.split("|")
money_spent = 0
total_money = 0
item_price = 0.0
item = ""
for i in range(len(items_list)):
    items_list[i] = items_list[i].split("->")
    item_price = float(items_list[i][1])
    item = items_list[i][0]
    if (item == "Clothes" and item_price > 50.00) or (item == "Shoes" and item_price > 35.00) or (item == "Accessories" and item_price > 20.50):
        continue
    if budget >= item_price:
        budget -= item_price
        money_spent += item_price
        print(f"{(item_price * 1.4):.2f}", end =" ")
    else:
        break

total_money = budget + money_spent * 1.4
print(f"\nProfit: {money_spent * 0.4:.2f}")
if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
