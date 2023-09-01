import math

num1_input = input("Enter a number:")
while True:
    try:
        float(num1_input)
        break
    except:
        print("Invalid input! You must enter a number!")
        num1_input = input("Enter a number:")

num1_input = float(num1_input)
result = num1_input

while True:

    command_input = input("Enter a command:")
    while command_input not in ["=", "+", "-", "*", "/", "^", "m", "log", "f"]:
        print("Invalid input!")
        command_input = input("Enter a command:")
    if command_input == "=":
        break

    num2_input = input("Enter a number:")
    while True:
        try:
            float(num2_input)
            break
        except:
            print("Invalid input! You must enter a number!")
            num2_input = input("Enter a number:")

    num2_input = float(num2_input)

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
