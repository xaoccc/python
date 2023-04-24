text = input()
text = [*text]
for char in sorted(list(set(text))):
    print(f"{char}: {text.count(char)} time/s")
