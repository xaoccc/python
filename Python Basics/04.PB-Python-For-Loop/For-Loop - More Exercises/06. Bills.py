#user input
months = int(input())
water_bill = 20
net_bill = 15
electricity_bill_sum = 0
water_bill_sum = 0
net_bill_sum = 0
others_bill_sum = 0

#logic
for i in range (1, months + 1) :
    electricity_bill = float(input())
    others_bill = (electricity_bill + water_bill + net_bill) * 1.2
    electricity_bill_sum += electricity_bill
    water_bill_sum += water_bill
    net_bill_sum += net_bill
    others_bill_sum += others_bill
avg_bill = (electricity_bill_sum + water_bill_sum + net_bill_sum + others_bill_sum) / months

#print output
print(f"Electricity: {electricity_bill_sum:.2f} lv")
print(f"Water: {water_bill_sum:.2f} lv")
print(f"Internet: {net_bill_sum:.2f} lv")
print(f"Other: {others_bill_sum:.2f} lv")
print(f"Average: {avg_bill:.2f} lv")
