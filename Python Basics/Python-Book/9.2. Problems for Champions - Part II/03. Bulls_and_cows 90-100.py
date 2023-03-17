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
        
        
# num = input()
# cows = int(input())
# bulls = int(input())
# cows_num_list = [0, 0, 0, 0, 0]
# bulls_num_list = [0, 0, 0, 0, 0]
# cows_list = []
# bulls_list = []

# for i in range(10000):
    
#     if len(str(i)) < 4:
#         i = str(i).zfill(4)
#     else:
#         i = str(i)
        
#     b = [i[0] == num[0], i[1] == num[1], i[2] == num[2], i[3] == num[3]]
#     c = [i[0] == num[1], 
#     i[0] == num[2], 
#     i[0] == num[3], 
#     i[1] == num[0], 
#     i[1] == num[2], 
#     i[1] == num[3], 
#     i[2] == num[0], 
#     i[2] == num[1], 
#     i[2] == num[3], 
#     i[3] == num[0], 
#     i[3] == num[1], 
#     i[3] == num[2]]

#     if i == num:
#         bulls_num_list[4] = 1
#         if bulls == 4:
#             bulls_list.append(i)
#     elif (b[0] and b[2] and b[3]) or (b[1] and b[2] and b[3]) or (b[0] and b[1] and b[3]) or (b[0] and b[1] and b[2]):
#         bulls_num_list[3] += 1
#         if bulls == 3:
#             bulls_list.append(i)
#     elif (b[0] and b[1]) or (b[0] and b[2]) or (b[0] and b[3]) or (b[1] and b[0]) or (b[1] and b[2]) or (b[1] and b[3]) or (b[2] and b[0]) or (b[2] and b[1]) or (b[2] and b[3]):
#         bulls_num_list[2] += 1
#         if bulls == 2:
#             bulls_list.append(i)
#     elif b[0] or b[1] or b[2] or b[3]:
#         bulls_num_list[1] += 1
#         if bulls == 1:
#             bulls_list.append(i)
#     else:
#         bulls_num_list[0] += 1
#         if bulls == 0:
#             bulls_list.append(i)
            
#     if (c[0] and c[3] and c[8] and c[11]) or (c[1] and c[3] and c[8] and c[10]) or (c[2] and c[3] and c[7] and c[11]) or (c[0] and c[4] and c[8] and c[9]):
#         cows_num_list[4] += 1
#         print(i)
#         if cows == 4:
#             cows_list.append(i)

        
# print(cows_num_list)
# print(bulls_num_list)
# print(cows_list)
# print(bulls_list)
