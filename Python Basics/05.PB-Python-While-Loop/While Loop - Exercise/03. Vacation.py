money_needed = float(input())
money_available = float(input())
spend_num = 0
days = 0

while money_available < money_needed:
    action = input()
    action_money = float(input())
    days += 1
    if action == "spend":
        money_available -= action_money
        if money_available < 0:
            money_available = 0
        spend_num += 1
    elif action == "save":
        money_available += action_money
        spend_num = 0
    if spend_num == 5:
        print("You can't save the money.")
        print(f"{days}")
        break
if money_available >= money_needed:
    print(f"You saved the money for {days} days.")