#user input
season = input().lower()
km_month = float(input())

#logic
if km_month <= 5000 :
    if season == "autumn" or season == "spring" :
        profit = km_month * 0.75
    elif season == "summer" :
        profit = km_month * 0.9
    elif season == "winter" :
        profit = km_month * 1.05
elif 5000 < km_month <= 10000 :
    if season == "autumn" or season == "spring" :
        profit = km_month * 0.95
    elif season == "summer" :
        profit = km_month * 1.1
    elif season == "winter" :
        profit = km_month * 1.25
elif 10000 < km_month <= 20000 :
    profit = km_month * 1.45
profit = profit * 4 * 0.9

#output
print(f"{profit:.2f}")