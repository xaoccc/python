dograma_num = int(input())
dograma_type = input()
delivery = input()
 
if dograma_type == "90X130":
    price = 110
    if dograma_num > 60:
        price *= 0.92
    elif dograma_num > 30:
        price *= 0.95
elif dograma_type == "100X150":
    price = 140
    if dograma_num > 80:
        price *= 0.90
    elif dograma_num > 40:
        price *= 0.94
elif dograma_type == "130X180":
    price = 190
    if dograma_num > 50:
        price *= 0.88
    elif dograma_num > 20:
        price *= 0.93
elif dograma_type == "200X300":
    price = 250
    if dograma_num > 50:
        price *= 0.86
    elif dograma_num > 25:
        price *= 0.91
total_price = dograma_num * price
if delivery == "With delivery":
    total_price += 60
if dograma_num > 99:
    total_price *= 0.96 
if dograma_num < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
