from math import ceil
guests = int(input())
budget = int(input())
kozun = 4
egg = 0.45
kozun_num = ceil(guests / 3)
eggs_num = ceil(guests * 2)
food_total_price = (kozun_num * kozun) + (eggs_num * egg)
 
if budget >= food_total_price:
    print(f"Lyubo bought {kozun_num} Easter bread and {eggs_num} eggs.")
    print(f"He has {budget - food_total_price:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {food_total_price - budget:.2f} lv. more.")
