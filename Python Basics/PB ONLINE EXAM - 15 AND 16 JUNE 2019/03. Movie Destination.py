budget = float(input())
dest = input()
season = input()
days = int(input())
 
if season == "Winter":
    if dest == "Dubai":
        price = 45000
    elif dest == "Sofia":
        price = 17000
    elif dest == "London":
        price = 24000
elif season == "Summer":
    if dest == "Dubai":
        price = 40000
    elif dest == "Sofia":
        price = 12500
    elif dest == "London":
        price = 20250
total_price = price * days
if dest == "Dubai":
    total_price *= 0.7
if dest == "Sofia":
    total_price *= 1.25
if budget >= total_price:
    print(f"The budget for the movie is enough! We have {budget - total_price:.2f} leva left!")
else:
    print(f"The director needs {total_price - budget:.2f} leva more!")
