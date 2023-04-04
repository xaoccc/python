nums = [int(i) for i in input().split()]
safe = []
for i in nums:
    safe.append(i)
result = []
total_result = []
if len(nums) == 1:
    print(nums[0])
elif len(nums) == 2:
    if nums[0] < nums[1]:
        print(*nums)
    else:
        print(nums[0])
else:
    for k in range(len(nums)-1):
        for j in range(len(nums)):
            current = nums[j]
            result = [current]
            for i in range(j+1, len(nums)):
                if nums[i] > current:
                    result.append(nums[i])
                    current = nums[i]
            total_result.append(result)
        nums.pop(k)
        if k > 1:
            nums.insert(k, safe[k])
        elif k == 1:
            nums.insert(k-1, safe[k-1])
    max_len = 0
    min_index = 100
    for i in total_result:      
        if len(i) > max_len:
            max_len = len(i)
            
    for i in total_result:
        if len(i) == max_len and safe.index(i[0]) < min_index:
            min_index = safe.index(i[0])
            
    for i in total_result: 
        if len(i) == max_len and safe.index(i[0]) == min_index:
            print(*i)
            break
