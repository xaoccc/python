drink = input()
sugar = input()
drinks_num = int(input())
total_price = 1
if sugar == "Without":
    total_price *= 0.65
if drink == "Espresso":
    if drinks_num > 5:
        total_price *= 0.75
    if sugar == "Without":
        total_price *= drinks_num * 0.9
    elif sugar == "Normal":
        total_price *= drinks_num * 1
    elif sugar == "Extra":
        total_price *= drinks_num * 1.2
elif drink == "Cappuccino":
    if sugar == "Without":
        total_price *= drinks_num * 1 
    elif sugar == "Normal":
        total_price *= drinks_num * 1.2
    elif sugar == "Extra":
        total_price *= drinks_num * 1.6
elif drink == "Tea":
    if sugar == "Without":
        total_price *= drinks_num * 0.5 
    elif sugar == "Normal":
        total_price *= drinks_num * 0.6
    elif sugar == "Extra":
        total_price *= drinks_num * 0.7
if total_price > 15:
    total_price *= 0.8
print(f"You bought {drinks_num} cups of {drink} for {total_price:.2f} lv.")
