#Amount should be default string and defined before the loop, because we use it in the check
amount = 0
#Total amount should be float!
amount_total = 0
#here we are starting the loop with checking the input
while amount != "NoMoreMoney" :
    amount = input()
    if amount == "NoMoreMoney":
        break
#Here is the tricky part - we convert the input to float, so we can make the valid amount check
    if float(amount) < 0 :
        print("Invalid operation!")
        break
#Here we sum all the valid inputs and store the sum in the variable amount_total
    amount_total += float(amount)
#Here is the second trucky part - me must convert the string variable "amount" to float, so we can use the formatting output :.2f
    print(f"Increase: {float(amount):.2f}")
#This the the final output with the total amount (after the loop is finished)
print(f"Total: {float(amount_total):.2f}")

#In while loops first we check the break conditions, then we procede with calculations. Is't like going to the shop - first you check if you put your shoes on, if not - return, then check if you have money - if not - return and after these both conditions are met, you procede with shopping.