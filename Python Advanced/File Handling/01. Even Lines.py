
with open('text.txt') as file:
    text = file.readlines()
symbols = ["-", ",", ".", "!", "?"]

for i in range(len(text)):
    if i % 2 == 0:
        for char in text[i]:
            if char in symbols:
                text[i] = text[i].replace(char, "@")
        result = text[i].split()
        result.reverse()
        print(" ".join(result))
