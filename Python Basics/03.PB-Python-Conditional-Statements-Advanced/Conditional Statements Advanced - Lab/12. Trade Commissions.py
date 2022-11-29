city = input().lower()
sales = float(input())
comm = 0
is_invalid_input = False

if  city == "sofia" :
    if 0 <= sales <= 500 :
        comm = 0.05
    elif 500 < sales <= 1000 :
        comm = 0.07
    elif 1000 < sales <= 10000 :
        comm = 0.08
    elif 10000 < sales :
        comm = 0.12
    else :
        is_invalid_input = True
elif city == "plovdiv" :
    if 0 <= sales <= 500 :
        comm = 0.055
    elif 500 < sales <= 1000 :
        comm = 0.08
    elif 1000 < sales <= 10000 :
        comm = 0.12
    elif 10000 < sales :
        comm = 0.145
    else :
        is_invalid_input = True
elif city == "varna" :
    if 0 <= sales <= 500 :
        comm = 0.045
    elif 500 < sales <= 1000 :
        comm = 0.075
    elif 1000 < sales <= 10000 :
        comm = 0.10
    elif 10000 < sales :
        comm = 0.13
    else :
        is_invalid_input = True
else :
    is_invalid_input = True

if is_invalid_input :
    print ("error")

else :         
    print (f"{(comm * sales):.2f}")


