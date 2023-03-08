import re

text_input = input().split()
pattern = r'^[A-Za-z0-9]+[a-zA-Z0-9\_.-]+[a-zA-Z0-9]+@[A-Za-z\-\.]+\.{1}[A-Za-z\-]+'
mail_list = []
for i in text_input:
    if ".." in i or "__" in i or "._" in i or "_." in i or "-." in i or  ".-" in i or "-_" in i or "_-" in i or "--" in i:
        continue
    mail_list += re.findall(pattern, i)

print(" ".join(mail_list))
