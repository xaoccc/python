coins = 0
change = float(input())
while change > 0:
    change = round(change, 2)
    if change >= 2:
        coins += 1
        change -= 2
    elif change >= 1:
        coins += 1
        change -= 1
    elif change >= 0.5:
        coins += 1
        change -= 0.5
    elif change >= 0.2:
        coins += 1
        change -= 0.2
    elif change >= 0.1:
        coins += 1
        change -= 0.1
    elif change >= 0.05:
        coins += 1
        change -= 0.05
    elif change >= 0.02:
        coins += 1
        change -= 0.02
    elif change >= 0.01:
        coins += 1
        change -= 0.01
    else:
        change = 0
print(coins)