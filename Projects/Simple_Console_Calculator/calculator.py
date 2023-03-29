import math

num1_input = float(input("Enter a number:"))
result = num1_input
while True:

    command_input = input("Enter a command:")
    if command_input == "=":
        break
    
    num2_input = float(input("Enter a number:"))

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
    elif command_input == "log":
        result = math.log(result)
        print(result)
    elif command_input == "f":
        result = math.factorial(int(result))
        print(result)

print(result)
