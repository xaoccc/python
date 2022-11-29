#input
n = int(input())
wash_mach_price = float(input())
toy_price = int(input())
sum_odd_age = 0
money = 0

#logic
#counting the years one by one
for i in range (0, n + 1) :
#checking for odd birthdays and counting them
    if i % 2 != 0 :
        sum_odd_age += 1
  
#checking for even birthdays
for i in range (1, n + 1) :
    if i % 2 == 0 :
        #summing the money for each even birthday
        money += 10 * (i/2)
        #the money which are taken each even birthday
        money -= 1
toys_profit = sum_odd_age * toy_price
money_diff = abs(wash_mach_price - toys_profit - money)

#user output
if wash_mach_price <= (toys_profit + money) :
    print(f"Yes! {money_diff:.2f}" )
else :
    print(f"No! {money_diff:.2f}" )

