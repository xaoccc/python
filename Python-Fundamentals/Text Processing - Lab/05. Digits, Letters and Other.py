sometext = input()
digits, chars, other = [], [], []

for i in sometext:
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        chars.append(i)
    else:
        other.append(i)
print(f"{''.join(digits)}\n{''.join(chars)}\n{''.join(other)}")
