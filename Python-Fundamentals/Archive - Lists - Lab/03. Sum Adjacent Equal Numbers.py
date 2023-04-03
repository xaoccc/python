nums = [float(item) for item in input().split(" ")]

i = 0
if len(nums) == 1:
    print(nums[0])
else:
    while i != len(nums):
        if nums[i - 1] == nums[i]:
            nums[i] = nums[i] + nums[i - 1]
            nums.remove(nums[i - 1])
            i = 0
        i += 1
    
    for num in nums:
        print(num, end=" ")
