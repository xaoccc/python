num = int(input())

for digit1 in range(1, 10):
    for digit2 in range(1, 10):
        for digit3 in range(1, 10):
            for digit4 in range(1, 10):
                if num % digit1 == 0 and num % digit2 == 0 and num % digit3 == 0 and num % digit4 == 0:
                    print(f"{str(digit1) + str(digit2) + str(digit3) + str(digit4)} ", end="")