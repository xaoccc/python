#user input
gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
fuel_type = input().lower()
fuel_q = float(input())
card = input().lower()

#logic
if card == "no" :
    if fuel_type == "gasoline" :
        fuel_price = gasoline_price * fuel_q
    elif fuel_type == "diesel" :
        fuel_price = diesel_price * fuel_q
    elif fuel_type == "gas" :
        fuel_price = gas_price * fuel_q
elif card == "yes" :
    if fuel_type == "gasoline" :
        fuel_price = (gasoline_price - 0.18) * fuel_q
    elif fuel_type == "diesel" :
        fuel_price = (diesel_price - 0.12) * fuel_q
    elif fuel_type == "gas" :
        fuel_price = (gas_price - 0.08) * fuel_q
if   20 <= fuel_q <= 25 :
    fuel_price = fuel_price*0.92
elif fuel_q > 25 :
    fuel_price = fuel_price*0.90
    
#output
print(f"{fuel_price:.2f} lv.")
