start = input()
end = input()
start1, start2, start3, start4 = int(start[0]), int(start[1]), int(start[2]), int(start[3])
end1, end2, end3, end4 = int(end[0]), int(end[1]), int(end[2]), int(end[3])
num1, num2, num3, num4 = 3, 3, 5, 5
 
for i in range(start1, end1 + 1):
    if i % 2 != 0:
        num1 = i
        i += 1
    else:
        i += 1
        continue
 
    for j in range(start2, end2 + 1):
        if j % 2 != 0:
            num2 = j
            j += 1
        else:
            j += 1
            continue
 
        for k in range(start3, end3 + 1):
            if k % 2 != 0:
                num3 = k
                k += 1
            else:
                k += 1
                continue
 
            for m in range(start4, end4 + 1):
                if m % 2 != 0:
                    num4 = m
                    m += 1
                else:
                    m += 1
                    continue
 
                print(f"{num1}{num2}{num3}{num4}", end=" ")
