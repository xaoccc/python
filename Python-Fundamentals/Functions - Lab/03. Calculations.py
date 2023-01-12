def calculator(operator = input(), first_num = int(input()), second_num = int(input())):
    if operator == "multiply":
        return first_num * second_num
    elif operator == "divide":
        return int(first_num / second_num)
    elif operator == "subtract":
        return first_num - second_num
    elif operator == "add":
        return first_num + second_num
        
print(calculator()) 
