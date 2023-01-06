#src: https://python-book.softuni.bg/chapter-09-problems-for-champions-part-2.html

num = input()
cows = int(input())
bulls = int(input())
    
digits_list = [int(num[0]), int(num[1]), int(num[2]), int(num[3])]

print(digits_list)

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
