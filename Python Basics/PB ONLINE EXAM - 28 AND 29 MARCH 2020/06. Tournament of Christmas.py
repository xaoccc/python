days_num = int(input())
money_total = 0
total_wins = 0
total_lose = 0
 
for i in range(days_num):
    money_day = 0
    loss_num = 0
    win_num = 0
 
    while True:
        game = input()
 
        if game == "Finish":
            total_wins += win_num
            total_lose += loss_num
            if win_num > loss_num:
                money_day *= 1.1
                money_total += money_day
            else:
                money_total += money_day
            break
 
        while True:
            result = input()
            if result == "lose":
                loss_num += 1
            else:
                win_num += 1
                money_day += 20
            break
 
if total_wins > total_lose:
    money_total *= 1.2
    print(f"You won the tournament! Total raised money: {money_total:.2f}")
 
else:
    print(f"You lost the tournament! Total raised money: {money_total:.2f}")
