#user input
budget = float(input())
category = input().lower()
people = int(input())
vip_price = 499.99 * people
normal_price = 249.99 * people

#logic and output
if people <= 4 :
    budget -= budget*0.75
elif 5 <= people <= 9 :
    budget -= budget*0.60
elif 10 <= people <= 24 :
    budget -= budget*0.50
elif 25 <= people <= 49 :
    budget -= budget*0.40
elif people >= 50 :
    budget -= budget*0.25
    
if category == "normal" :
    if budget >= normal_price :
        money_left = budget - normal_price
        print(f"Yes! You have {money_left:.2f} leva left.")
    else :
        money_needed = normal_price - budget
        print(f"Not enough money! You need {money_needed:.2f} leva.")
if category == "vip" :
    if budget >= vip_price : 
        money_left = budget - vip_price 
        print(f"Yes! You have {money_left:.2f} leva left.")
    else :
        money_needed = vip_price - budget
        print(f"Not enough money! You need {money_needed:.2f} leva.")
