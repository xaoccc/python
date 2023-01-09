#src: https://python-book.softuni.bg/chapter-09-problems-for-champions-part-2.html

num = input()
cows = int(input())
bulls = int(input())
bulls_found = 0
cows_found = 0

solution_found = False

if bulls > 4 or cows > 4:
    solution_found = False
else:
    digits_list = [int(num[0]), int(num[1]), int(num[2]), int(num[3])]
    for digit_1 in range(1, 10):
        for digit_2 in range(1, 10):
            for digit_3 in range(1, 10):
                for digit_4 in range(1, 10):
                    digit_to_check_1 = digit_1
                    digit_to_check_2 = digit_2
                    digit_to_check_3 = digit_3
                    digit_to_check_4 = digit_4 
                    if digit_to_check_1 == digits_list[0]:
                        bulls_found += 1
                        digits_list[0] = -1
                        digit_to_check_1 = -2
                    if digit_to_check_2 == digits_list[1]:
                        bulls_found += 1
                        digits_list[1] = -1
                        digit_to_check_2 = -2
                    if digit_to_check_3 == digits_list[2]:
                        bulls_found += 1
                        digits_list[2] = -1
                        digit_to_check_3 = -2
                    if digit_to_check_4 == digits_list[3]:
                        bulls_found += 1
                        digits_list[3] = -1
                        digit_to_check_4 = -2
                        
                    if digit_to_check_1 == digits_list[1]:
                        cows_found += 1
                        digits_list[1] = -1
                    if digit_to_check_1 == digits_list[2]:
                        cows_found += 1
                        digits_list[2] = -1
                    if digit_to_check_1 == digits_list[3]:
                        cows_found += 1
                        digits_list[3] = -1
                        
                    if digit_to_check_2 == digits_list[0]:
                        cows_found += 1
                        digits_list[0] = -1
                    if digit_to_check_2 == digits_list[2]:
                        cows_found += 1
                        digits_list[2] = -1
                    if digit_to_check_2 == digits_list[3]:
                        cows_found += 1
                        digits_list[3] = -1
                        
                    if digit_to_check_3 == digits_list[0]:
                        cows_found += 1
                        digits_list[0] = -1
                    if digit_to_check_3 == digits_list[1]:
                        cows_found += 1
                        digits_list[1] = -1
                    if digit_to_check_3 == digits_list[3]:
                        cows_found += 1
                        digits_list[3] = -1
                        
                    if digit_to_check_4 == digits_list[0]:
                        cows_found += 1
                        digits_list[0] = -1
                    if digit_to_check_4 == digits_list[1]:
                        cows_found += 1
                        digits_list[1] = -1
                    if digit_to_check_4 == digits_list[2]:
                        cows_found += 1
                        digits_list[2] = -1

                        
                    if cows == cows_found and bulls == bulls_found:
                        print("%d%d%d%d" % (digit_1, digit_2, digit_3, digit_4), end="")
    
    
if not solution_found:
    print("No")

    
