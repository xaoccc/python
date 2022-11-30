city = input()
package = input()
vip = input()
days = int(input())
 
if days > 7:
    days -= 1
if days < 1:
    print("Days must be positive number!")
elif city == "Bansko" or city == "Borovets" :
    if package == "withEquipment":
        price_day = 100
        vip_discount = 0.1
        total_price = days * price_day * (1 - vip_discount)
        if vip == "no":
            total_price = days * price_day
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
    elif package == "noEquipment":
        price_day = 80
        vip_discount = 0.05
        total_price = days * price_day * (1 - vip_discount)
        if vip == "no":
            total_price = days * price_day
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
    else :
        print ("Invalid input!")
elif city == "Varna" or city == "Burgas" :
    if package == "withBreakfast":
        price_day = 130
        vip_discount = 0.12
        total_price = days * price_day * (1 - vip_discount)
        if vip == "no":
            total_price = days * price_day
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
    elif package == "noBreakfast":
        price_day = 100
        vip_discount = 0.07
        total_price = days * price_day * (1 - vip_discount)
        if vip == "no":
            total_price = days * price_day
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
    else :
        print ("Invalid input!")
else :
    print ("Invalid input!")
