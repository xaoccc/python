stage = input()
ticket_type = input()
ticket_num = int(input())
pic = input()
price = 1
 
if stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.90
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40
elif stage == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400
total = ticket_num * price
if 2500 < total <= 4000:
    total *= 0.9
if pic == "Y" and total <= 4000:
    total += ticket_num * 40
elif total > 4000:
    total *= 0.75
 
print(f"{total:.2f}")
