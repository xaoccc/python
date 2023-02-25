words_num = int(input())
dictionary = {}

for i in range(words_num):
    current_word = input()
    synonym = input()
    if current_word not in dictionary:
        dictionary[current_word] = []
    dictionary[current_word].append(synonym)
    
for (key, value) in dictionary.items():
    print(f"{key} - {', '.join(value)}")
