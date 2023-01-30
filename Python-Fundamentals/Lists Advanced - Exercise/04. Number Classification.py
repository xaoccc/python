nums = input().split(", ")
nums = [int(i) for i in nums]
positive, negative, even, odd = [], [], [], []
for num in nums:
    if num % 2 == 0:
        even.append(num)
    if num % 2 != 0:
        odd.append(num)
    if num < 0:
        negative.append(num)
    if num >= 0:
        positive.append(num)
positive = [str(i) for i in positive]
negative = [str(i) for i in negative]
even = [str(i) for i in even]
odd = [str(i) for i in odd]
positive, negative, even, odd = ", ".join(positive), ", ".join(negative), ", ".join(even), ", ".join(odd)   
print(f"Positive: {positive}\nNegative: {negative}\nEven: {even}\nOdd: {odd}")
