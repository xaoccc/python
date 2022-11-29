limit_num1 = int(input())
limit_num2 = int(input())
limit_num3 = int(input())

for num1 in range(1, limit_num1 + 1):
    for num2 in range(1, limit_num2 + 1):
        if num2 == 1 or num2 == 4 or num2 == 6 or num2 > 7:
            continue
        for num3 in range(1, limit_num3 + 1):
            if num1 % 2 != 0 or num3 % 2 != 0:
                continue
            print(str(num1) + " " + str(num2) + " " + str(num3))