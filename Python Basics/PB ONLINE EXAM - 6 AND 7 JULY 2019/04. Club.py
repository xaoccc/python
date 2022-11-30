win = float(input())
profit = 0
profit_total = 0
while win > profit_total:
    cocktail = input()
    if cocktail == "Party!":
        print(f"We need {win - profit_total:.2f} leva more.")
        break
    cocktail_num = int(input())
    cocktail_price = len(cocktail)
    profit = cocktail_num * cocktail_price
    if profit % 2 != 0:
        profit *= 0.75
    profit_total += profit
 
if win <= profit_total:
    print("Target acquired.")
print(f"Club income - {profit_total:.2f} leva.")
