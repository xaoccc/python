def calculator(operator, first_num, second_num ):
    if operator == "multiply":
        return first_num * second_num
    elif operator == "divide":
        return int(first_num / second_num)
    elif operator == "subtract":
        return first_num - second_num
    elif operator == "add":
        return first_num + second_num
        
print(calculator(input(),int(input()),int(input())))
