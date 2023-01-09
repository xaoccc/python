#src: https://python-book.softuni.bg/chapter-09-problems-for-champions-part-2.html

from decimal import Decimal

available_money = Decimal(input())
command = input()
 
while command != "mall.Enter":
    command = input()

number_purchases = 0
action = ""
 
while action != "mall.Exit":
 
    for symbol in range(len(action)):
 
        if 65 <= ord(action[symbol]) <= 90:
            cost_of_purchase = ord(action[symbol]) * Decimal(0.50)
            if cost_of_purchase <= available_money:
                available_money -= cost_of_purchase
                number_purchases += 1
 
        elif 97 <= ord(action[symbol]) <= 122:
            cost_of_purchase = ord(action[symbol]) * Decimal(0.30)
            if cost_of_purchase <= available_money:
                available_money -= cost_of_purchase
                number_purchases += 1
 
        elif action[symbol] == "%":
            if available_money != 0:
                available_money *= Decimal(0.50)
                number_purchases += 1
 
        elif action[symbol] == "*":
            available_money += 10
 
        else:
            cost_of_purchase = ord(action[symbol])
            if cost_of_purchase <= available_money:
                available_money -= cost_of_purchase
                number_purchases += 1
 
    action = input()
 
if number_purchases == 0:
    print(f"No purchases. Money left: {available_money:.2f} lv.")
else:
    print(f"{number_purchases} purchases. Money left: {available_money:.2f} lv.")
