num = input()
bulls = int(input())
cows = int(input())
solution_found = False

for digit_1 in range(1, 10):
    for digit_2 in range(1, 10):
        for digit_3 in range(1, 10):
            for digit_4 in range(1, 10):
                guess_digit_1 = int(num[0])
                guess_digit_2 = int(num[1])
                guess_digit_3 = int(num[2])
                guess_digit_4 = int(num[3])
                
                digit_to_check_1 = digit_1
                digit_to_check_2 = digit_2
                digit_to_check_3 = digit_3
                digit_to_check_4 = digit_4
                bulls_num = 0
                cows_num = 0
                if digit_to_check_1 == guess_digit_1:
                    bulls_num += 1
                    guess_digit_1 = -1
                    digit_to_check_1 = -2
                if digit_to_check_2 == guess_digit_2:
                    bulls_num += 1
                    guess_digit_2 = -1
                    digit_to_check_2 = -2
                if digit_to_check_3 == guess_digit_3:
                    bulls_num += 1
                    guess_digit_3 = -1
                    digit_to_check_3 = -2
                if digit_to_check_4 == guess_digit_4:
                    bulls_num += 1
                    guess_digit_4 = -1
                    digit_to_check_4 = -2
                    
                if digit_to_check_1 == guess_digit_2:
                    cows_num += 1
                    guess_digit_2 = -1
                elif digit_to_check_1 == guess_digit_3:
                    cows_num += 1
                    guess_digit_3 = -1
                elif digit_to_check_1 == guess_digit_4:
                    cows_num += 1
                    guess_digit_4 = -1
                    
                if digit_to_check_2 == guess_digit_1:
                    cows_num += 1
                    guess_digit_1 = -1
                elif digit_to_check_2 == guess_digit_3:
                    cows_num += 1
                    guess_digit_3 = -1
                elif digit_to_check_2 == guess_digit_4:
                    cows_num += 1
                    guess_digit_4 = -1
                    
                if digit_to_check_3 == guess_digit_1:
                    cows_num += 1
                    guess_digit_1 = -1
                elif digit_to_check_3 == guess_digit_2:
                    cows_num += 1
                    guess_digit_2 = -1
                elif digit_to_check_3 == guess_digit_4:
                    cows_num += 1
                    guess_digit_4 = -1
                    
                if digit_to_check_4 == guess_digit_1:
                    cows_num += 1
                    guess_digit_1 = -1
                elif digit_to_check_4 == guess_digit_2:
                    cows_num += 1
                    guess_digit_2 = -1
                elif digit_to_check_4 == guess_digit_3:
                    cows_num += 1
                    guess_digit_3 = -1
                
                if cows == cows_num and bulls == bulls_num:
                    if solution_found:
                        print(" ", end="")
                    print(f"{digit_1}{digit_2}{digit_3}{digit_4}", end="")
                    solution_found = True
                
if not solution_found:
    print("No")

    
