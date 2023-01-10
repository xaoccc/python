num = input()
bulls = int(input())
cows = int(input())
num_stored = num
solution_found = False
numcheck = ""
if bulls > 4 or cows > 4:
    solution_found = False
    print("No")
elif bulls == 4 and cows == 0:
    solution_found = True
    print(num)
else:    
    for _ in range(1111, 10000):
        num = num_stored
        if str(_)[1] == "0" or str(_)[2] == "0" or str(_)[3] == "0":
            continue
        bulls_found = 0
        cows_found = 0
        numcheck = [str(_).rjust(4, '0')]
    
        for i in range(4):
            if numcheck[0][i] == num[i]:
                bulls_found += 1
                num = num[:i] + "a" + num[i + 1:]
                numcheck[0] = numcheck[0][:i] + "b" + numcheck[0][i + 1:]
                
        if bulls_found > bulls:
            continue
                
        for j in range(1,4):
            if numcheck[0][0] == num[j]:
                cows_found += 1
                num = num[:j] + "a" + num[j + 1:]
    
        if numcheck[0][1] == num[0]:
            cows_found += 1
            num = num[:0] + "a" + num[0 + 1:]
        if numcheck[0][1] == num[2]:
            cows_found += 1
            num = num[:2] + "a" + num[2 + 1:]
        if numcheck[0][1] == num[3]:
            cows_found += 1
            num = num[:3] + "a" + num[3 + 1:]
            
        for l in range(-1, 2):
            if numcheck[0][2] == num[l]:
                cows_found += 1
                num = num[:l] + "a" + num[l + 1:]
        
        for k in range(3):    
            if numcheck[0][3] == num[k]:
                cows_found += 1
                num[:k] + "a" + num[k + 1:]
    
        if cows == cows_found and bulls == bulls_found:
            solution_found = True
            print(f"{_} ", end="")
        
    if not solution_found:
        print("No")
