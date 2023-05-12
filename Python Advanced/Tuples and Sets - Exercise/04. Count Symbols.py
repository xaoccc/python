text = [*input()]
for char in sorted(set(text)):
    print(f"{char}: {text.count(char)} time/s")
    
# occurences = {}
# for letter in input():
#     occurences[letter] = occurences.get(letter, 0) + 1
# for letter, times in sorted(occurences.items()):
#     print(f"{letter}: {times} time/s")


