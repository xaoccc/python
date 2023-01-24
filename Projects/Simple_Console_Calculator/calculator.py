num1_input = float(input())
result = num1_input
while True:

    command_input = input()
    if command_input == "=":
        break
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
    elif command_input == "modul":
        result %= num2_input
        print(result)

print(result)
