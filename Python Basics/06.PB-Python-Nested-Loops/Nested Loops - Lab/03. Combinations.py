n = int(input())
n_count = 0
for num1 in range(0, n + 1):
    for num2 in range(0, n + 1):
        for num3 in range(0, n + 1):
            if (num1 + num2 + num3) == n:
                n_count += 1 
print(n_count)