def small_number(number):
    nums = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    return nums[number]


def teens(number):
    nums = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    return nums[number]

def tens(number):
    nums = {
        2: "twenty",
        3: "thirty",
        4: "fourty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }
    return nums[number]


def letterize(number):
    result = ""
    if number > 999:
        return "too large"
    elif number < -999:
        return "too small"
    else:
        original_number = number
        number = abs(number)
        if number < 10:
            result = small_number(number)
        elif 9 < number < 20:
            result = teens(number)
        elif 19 < number < 100:
            if number // 10 == 0:
                result = tens(number)
            else:
                result = tens(number // 10) + " " + small_number(number % 10)
        else:
            result = small_number(number // 100) + "-hundred"
            if number % 100 != 0:
                result += " and "
                if number % 100 > 19:
                    result += tens(number % 100 // 10)
                    if number % 10 != 0:
                        result += " " + small_number(number % 10)
                elif number % 100 > 9:
                    result += teens(number % 100)
                else:
                    result += small_number(number % 100)
                
        if original_number > 0:
            return result
        else:
            return "minus " + result

for i in range(int(input())):
    print(letterize(int(input())))
