import re

text = input()
while text:
    pattern = r'(\bwww\.[a-zA-Z0-9]+(\.[a-zA-Z0-9]+|\-[a-zA-Z0-9]+)*\.[a-z]+(\.[a-z]+)*\b)'
    link = re.finditer(pattern, text)
    for i in link:
        print(i.group())
    text = input()
