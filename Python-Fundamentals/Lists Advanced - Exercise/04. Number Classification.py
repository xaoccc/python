nums =[int(i) for i in input().split(", ")]

positive, negative, even, odd = [], [], [], []
for num in nums:
    if num % 2 == 0:
        even.append(str(num))
    if num % 2 != 0:
        odd.append(str(num))
    if num < 0:
        negative.append(str(num))
    if num >= 0:
        positive.append(str(num))

positive, negative, even, odd = ", ".join(positive), ", ".join(negative), ", ".join(even), ", ".join(odd)   
print(f"Positive: {positive}\nNegative: {negative}\nEven: {even}\nOdd: {odd}")
