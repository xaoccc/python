#input
luggage_price_20 = float(input())
luggage_kg = float(input())
days = int(input())
luggage_num = int(input())

#logic
if luggage_kg < 10:
    luggage_price = luggage_price_20 * 0.2 
elif 10 <= luggage_kg <= 20:
    luggage_price = luggage_price_20 * 0.5
else:
    luggage_price = luggage_price_20
if days > 30:
    luggage_price *= 1.1
elif days >= 7:
    luggage_price *= 1.15
else:
    luggage_price *= 1.4
total = luggage_price * luggage_num

#output
print(f" The total price of bags is: {total:.2f} lv. ")
