nums = [int(i) for i in input().split()]
command = input()

while command != "print":
    command = command.split()
    if command[0] == "add":
        nums.insert(int(command[1]), int(command[2]))
        
    elif command[0] == "addMany":
        addmany = [int(i) for i in command[2:]]
        nums = nums[:int(command[1])] + addmany + nums[int(command[1]):]
        
    elif command[0] == "contains":
        if int(command[1]) in nums:
            print(nums.index(int(command[1])))
        else:
            print(-1)
            
    elif command[0] == "remove":
        nums.pop(int(command[1]))
        
    elif command[0] == "shift": 
        if int(command[1]) <= len(nums):
            nums = nums[int(command[1]):] + nums[:int(command[1])]
        else:
            nums = nums[int(command[1]) % len(nums):] + nums[:int(command[1]) % len(nums) ]
        
    elif command[0] == "sumPairs": 
        sum_pairs = []
        for i in range(0, len(nums)-1, 2):
            sum_pairs.append(nums[i]+nums[i+1])
        if len(nums) % 2 != 0:
            sum_pairs.append(nums[-1])
        nums = sum_pairs
    
    command = input()
print(nums)
