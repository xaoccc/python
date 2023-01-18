def pass_validator():
    nums_input = input()
    digits_num = 0
    
    for i in range(len(nums_input)):
        if nums_input[i].isdigit():
            digits_num += 1
    if len(nums_input) < 6 or len(nums_input) > 10:
        print("Password must be between 6 and 10 characters")
    if not nums_input.isalnum():
        print("Password must consist only of letters and digits")
    if digits_num < 2:
        print("Password must have at least 2 digits")
    if (5 < len(nums_input) < 11) and nums_input.isalnum() and digits_num > 1:
        print("Password is valid")

pass_validator()
