#user input
wallet = float(input())
nvidia = int(input())
intel = int(input())
ddr6 = int(input())

#logic
nvidia_price = 250
intel_price = nvidia_price * nvidia * 0.35
ddr6_price = nvidia_price * nvidia * 0.10
bill = (nvidia * nvidia_price) + (intel * intel_price) + (ddr6 * ddr6_price)

#output
if nvidia > intel :
    bill = bill - (bill * 0.15)
    if bill > wallet :
        print (f"Not enough money! You need {bill-wallet:.2f} leva more!")
    else :
        print (f"You have {wallet-bill:.2f} leva left!")
else :
    if bill > wallet :
        print (f"Not enough money! You need {bill-wallet:.2f} leva more!")
    else :
        print (f"You have {wallet-bill:.2f} leva left!")
