result = []
max_len = 1
max_len_list = []

nums = [int(i) for i in input().split()]

if len(nums) == len(set(nums)):
    print(nums[0])
    
else:
    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            result.append([nums[i-1], nums[i]])

    if len(result) == 0:
        print(nums[0])
        
    else:
        i = 0 
        if len(result) == 1:
            print(*result[0])
        
        else:
            while True:
                if result[i-1][0] == result[i][0]:
                    result[i-1].append(result[i][0])
                    del result[i]
                    i = 0
                
                if i < len(result) - 1:
                    i += 1
                else:
                    break
       
            for i in result:
                if max_len < len(i):
                    max_len = len(i)
                    max_len_list = i
                
            print(*max_len_list)
