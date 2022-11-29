num1 = int(input())
num2 = int(input())
result = ""

for i in range(num1, num2 + 1):
    for j in range(num1, num2 + 1):
        for k in range(num1, num2 + 1):
            if (j + k) % 2 != 0:
                continue
            for l in range(num1, num2 + 1):
                if ((i % 2 == 0 and l % 2 != 0) or (i % 2 != 0 and l % 2 == 0)) and (i > l):
                    print (str(i) + str(j) + str(k) + str(l), end = " ")
                else:
                    continue