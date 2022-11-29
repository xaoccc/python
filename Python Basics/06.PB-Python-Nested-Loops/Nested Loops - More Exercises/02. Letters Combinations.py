letter1 = input()
letter2 = input()
letter3 = input()
combination_num = 0

for i in range(ord(letter1), ord(letter2) + 1):
    if i == ord(letter3):
        continue
    for j in range(ord(letter1), ord(letter2) + 1):
        if j == ord(letter3):
            continue
        for k in range(ord(letter1), ord(letter2) + 1):
            if k == ord(letter3):
                continue
            combination_num += 1
            print(chr(i) + chr(j) + chr(k), end=" ")
print(combination_num)