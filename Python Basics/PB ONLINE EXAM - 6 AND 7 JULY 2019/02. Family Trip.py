budget = float(input())
nights = int(input())
night_price = float(input())
add_price_perc = int(input())
 
if nights > 7:
    night_price *= 0.95
add_price = budget * add_price_perc / 100
total_price = (nights * night_price) + add_price
money_left = abs(budget - total_price)
if budget >= total_price :
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    print(f"{money_left:.2f} leva needed.")
