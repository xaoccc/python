import re
uppercase = []
lowercase = []
mixed = []
separators = r"[,;:.!()\x22\x27\\/[\]\s]"
words = re.split(separators, input())
words = [word for word in words if word]

for word in words:
    if word.isupper() and word.isalpha():
        uppercase.append(word)
    elif word.islower() and word.isalpha():
        lowercase.append(word)
    else:
        mixed.append(word)
uppercase = ", ".join(uppercase)
lowercase = ", ".join(lowercase)
mixed = ", ".join(mixed)
print(f"Lower-case: {lowercase}\nMixed-case: {mixed}\nUpper-case: {uppercase}")
