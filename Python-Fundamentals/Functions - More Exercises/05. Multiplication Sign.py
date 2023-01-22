def multi_sign(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        print("zero")
    elif num1 < 0: 
        if num2 > 0:
            if num3 > 0:
                print("negative")
            else:
                print("positive")
        else:
            if num3 > 0:
                print("positive")
            else:
                print("negative")
    else:
        if num2 > 0:
            if num3 > 0:
                print("positive")
            else:
                print("negative")
        else:
            if num3 > 0:
                print("negative")
            else:
                print("positive")
                
multi_sign(int(input()), int(input()), int(input()))
