num = input()
bulls = int(input())
cows = int(input())
num_stored = num
solution_found = False
numcheck = ""

for i in range(1111, 9999):
    num = num_stored
    if str(i)[1] == "0" or str(i)[2] == "0" or str(i)[3] == "0":
        continue
    bulls_found = 0
    cows_found = 0
    numcheck = [str(i).rjust(4, '0')]
    if numcheck[0][0] == num[0]:
        bulls_found += 1
        num = num.replace(num[0], "a")
    if numcheck[0][1] == num[1]:
        bulls_found += 1
        num = num.replace(num[1], "a")
    if numcheck[0][2] == num[2]:
        bulls_found += 1
        num = num.replace(num[2], "a")
    if numcheck[0][3] == num[3]:
        bulls_found += 1
        num = num.replace(num[3], "a")
        
        
    if numcheck[0][0] == num[1]:
        cows_found += 1
        num = num.replace(num[1], "a")
    if numcheck[0][0] == num[2]:
        cows_found += 1
        num = num.replace(num[2], "a")
    if numcheck[0][0] == num[3]:
        cows_found += 1
        num = num.replace(num[3], "a")
        
    if numcheck[0][1] == num[0]:
        cows_found += 1
        num = num.replace(num[0], "a")
    if numcheck[0][1] == num[2]:
        cows_found += 1
        num = num.replace(num[2], "a")
    if numcheck[0][1] == num[3]:
        cows_found += 1
        num = num.replace(num[3], "a")
        
    if numcheck[0][2] == num[0]:
        cows_found += 1
        num = num.replace(num[0], "a")
    if numcheck[0][2] == num[1]:
        cows_found += 1
        num = num.replace(num[1], "a")
    if numcheck[0][2] == num[3]:
        cows_found += 1
        num = num.replace(num[3], "a")
        
    if numcheck[0][3] == num[0]:
        cows_found += 1
        num = num.replace(num[0], "a")
    if numcheck[0][3] == num[1]:
        cows_found += 1
        num = num.replace(num[1], "a")
    if numcheck[0][3] == num[2]:
        cows_found += 1
        num = num.replace(num[2], "a")


    if cows == cows_found and bulls == bulls_found:
        solution_found = True
        print(f"{numcheck[0]} ", end="")
        
if not solution_found:
    print("No")
