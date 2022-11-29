#user input
vacation_cost = float(input())
puzzle_num = int(input())
doll_num = int(input())
bear_num = int(input())
minion_num = int(input())
truck_num = int(input())

#logic
full_num = puzzle_num + doll_num + bear_num + minion_num + truck_num
if full_num >= 50:
    discount = 0.25
else:
discount = 0
puzzle_num *= 2.60
doll_num *= 3
bear_num *= 4.10
minion_num *= 8.20
truck_num *= 2
full_profit = puzzle_num + doll_num + bear_num + minion_num + truck_num
full_profit = full_profit - (full_profit * discount)
budget = full_profit - (full_profit * 0.10)

#print output
if budget < vacation_cost:
    cost = vacation_cost - budget
    print(f'Not enough money! {cost:.2f} lv needed.')
elif budget >= vacation_cost:
    cost = budget - vacation_cost
    print(f'Yes! {cost:.2f} lv left.')
