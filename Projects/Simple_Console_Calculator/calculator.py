import math

num1_input = float(input())
result = num1_input
while True:

    command_input = input()
    if command_input == "=":
        break
    elif command_input == "log":
        result = math.log(result)
        print(result)
        continue
    elif command_input == "f":
        result = math.factorial(int(result))
        print(result)
        continue
    
    num2_input = float(input())

    if command_input == "+":
        result += num2_input
        print(result)
    elif command_input == "-":
        result -= num2_input
        print(result)
    elif command_input == "*":
        result *= num2_input
        print(result)
    elif command_input == "/":
        result /= num2_input
        print(result)
    elif command_input == "^":
        result **= num2_input
        print(result)
    elif command_input == "m":
        result %= num2_input
        print(result)
        
print(result)
