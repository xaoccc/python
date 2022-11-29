budget = float(input())
series = int(input())
series_price_sum = 0
 
for i in range(0, series):
    series_name = input()
    series_price = float(input())
    if series_name == "Thrones":
        series_price *= 0.5
    elif series_name == "Lucifer":
        series_price *= 0.6
    elif series_name == "Protector":
        series_price *= 0.7
    elif series_name == "TotalDrama":
        series_price *= 0.8
    elif series_name == "Area":
        series_price *= 0.9
    series_price_sum += series_price
 
if budget >= series_price_sum:
    print(f"You bought all the series and left with {budget - series_price_sum:.2f} lv.")
else:
    print(f"You need {series_price_sum - budget:.2f} lv. more to buy the series!")
