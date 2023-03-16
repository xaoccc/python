import re
words, w_list, mirror = input(), [], {}
words_list = re.finditer(r"([\@\#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1", words)
result = ""

for i in words_list:
    if i.group()[0] == i.group()[-1]:
        w_list.append(i.group())

for i in w_list:
    if i[1:(len(i)//2) - 1] == i[(len(i)//2) + 1 : -1][::-1]:
        mirror[i[1:(len(i)//2) - 1]] = i[(len(i)//2) + 1 : -1]

if len(w_list) == 0:
    print("No word pairs found!")
else:
    print(f"{len(w_list)} word pairs found!")         

if len(mirror) > 0:
    print("The mirror words are:")
    for word, reversed_word in mirror.items():
        result += f"{word} <=> {reversed_word}, "
    print(result[:-2])
else:
    print("No mirror words!")
