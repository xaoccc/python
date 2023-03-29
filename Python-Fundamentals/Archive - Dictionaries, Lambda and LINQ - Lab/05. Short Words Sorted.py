no_chars = [".", ",", ":", ";", "(", ")", "[", "]", '"', "'", "\\", "/", "!", "?" ]
result = []
string = input()
for i in string:
    if i in no_chars:
        string = string.replace(i, "")

for i in string.split():
    if len(i) < 5:
        result.append(i.lower())
print(*sorted(set(result)), sep=", ")
