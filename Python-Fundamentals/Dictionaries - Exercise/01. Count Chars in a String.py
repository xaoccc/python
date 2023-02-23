text = input().replace(" ","")
dictionary = {}
for i in range(len(text)):
    if text[i] not in dictionary:
        dictionary[text[i]] = 0
    dictionary[text[i]] += 1
for (key, value) in dictionary.items():
    print(f"{key} -> {value}")
