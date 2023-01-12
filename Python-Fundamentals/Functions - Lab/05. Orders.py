def order(order_type = input(), qty = int(input())):
    if order_type == "coffee":
        return qty * 1.5
    elif order_type == "water":
        return qty * 1
    elif order_type == "coke":
        return qty * 1.4
    else:
        return qty * 2
print(f"{order():.2f}")
