words = input().split()
dictionary = {}

for i in words:
    i = i.lower()
    if i not in dictionary:
        dictionary[i] = []
    dictionary[i].append(i)

for i in dictionary:
    if len(dictionary[i]) % 2 != 0:
        print(i, end=" ")

        
# words = input().split()
# dictionary = {}

# for i in words:
#     i = i.lower()
#     if i not in dictionary:
#         dictionary[i] = 0
#     dictionary[i] += 1

# for (key, value) in dictionary.items():
#     if value % 2 != 0:
#         print(key, end=" ")
