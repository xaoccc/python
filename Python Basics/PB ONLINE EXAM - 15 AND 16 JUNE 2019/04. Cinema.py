#input
capacity = int(input())
fans_num = 0
price = 5
total_income = 0
 
#logic
while fans_num <= capacity:
#loop input should be string, because of the command "Movie time!"
    fans_entered = input()
#the first breakpoint check should be right after the input, so the income data will not include the current fans_entered/income
    if fans_entered == "Movie time!":
        print(f"There are {capacity - fans_num} seats left in the cinema.")
        break
#the fans_num counter should be after the first breakpoint and right before the second one, because this is the condition of the second breakpoint
    fans_num += int(fans_entered)
#fans_num is turned into int for the purpose of calculations. If we enter a string, different from "Movie time!", the code will crash!
    if int(fans_num) > capacity:
        print("The cinema is full.")
        break
#if income calculator is not here, but on earlier point in the loop, the program will count additional income from people who could'n enter in the cinema, because it was full
    income = int(fans_entered) * price
    if int(fans_entered) % 3 == 0:
        income -= 5
    total_income += income
 
print(f"Cinema income - {total_income} lv.")
