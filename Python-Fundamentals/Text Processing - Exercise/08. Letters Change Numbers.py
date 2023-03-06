import string
low, up = string.ascii_lowercase, string.ascii_uppercase
text = input().split()
current_result, total = 0, 0

for i in text:
    if i[1:-1].isdigit():
        if i[0].isupper():
            current_result = int(i[1:-1]) / (up.index(i[0]) + 1)
        if i[0].islower():
            current_result = int(i[1:-1]) * (low.index(i[0]) + 1)
        if i[-1].isupper():
            current_result -= (up.index(i[-1]) + 1)
        if i[-1].islower():
            current_result += (low.index(i[-1]) + 1)
        total += current_result 
        
print(f"{total:.2f}")
