from math import sqrt
result = []
nums = [int(i) for i in input().split()]
for num in nums:
    if sqrt(num) == int(sqrt(num)):
        result.append(num)
result = sorted(result)
result.reverse() 
print(*result)
