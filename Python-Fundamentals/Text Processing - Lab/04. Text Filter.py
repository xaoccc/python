banned_words = input().split(", ")
sometext = input()
for word in banned_words:
    while word in sometext:
        sometext = sometext.replace(word, "*" * len(word))
print(sometext)
