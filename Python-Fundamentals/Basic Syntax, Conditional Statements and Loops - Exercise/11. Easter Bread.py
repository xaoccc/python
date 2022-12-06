budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 * 0.25
loaf_price = flour_price + eggs_price + milk_price
loaf_num = int(budget // loaf_price)
money_left = budget % loaf_price
colored_eggs_num = 0

for i in range(1, loaf_num + 1):
  colored_eggs_num += 3
  if i % 3 == 0:
    colored_eggs_num -= i - 2
    
print(f"You made {loaf_num} loaves of Easter bread! Now you have {colored_eggs_num} eggs and {money_left:.2f}BGN left.")
