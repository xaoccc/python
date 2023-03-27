budget = float(input())
initial_capital = float(input())
investors_num = int(input())

investors_money_sum = initial_capital

for i in range(1, investors_num + 1):
    investors_money = float(input())
    print(f"Investor {i} gave us {investors_money:.2f}.")
    investors_money_sum += investors_money
    if investors_money_sum >= budget:
        print(f"We will manage to build it. Start now! Extra money - {investors_money_sum - budget:.2f}.")
        break
if investors_money_sum < budget:
    print(f"Project can not start. We need {budget - investors_money_sum:.2f} more.")
