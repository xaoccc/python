import re

text = input()
while text:
    pattern = r'(^|(?<=\s))www\.[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)*\.[a-z]+(\.[a-z]+)*($|(?=\s))'
    link = re.finditer(pattern, text)
    for i in link:
        print(i.group())
    text = input()