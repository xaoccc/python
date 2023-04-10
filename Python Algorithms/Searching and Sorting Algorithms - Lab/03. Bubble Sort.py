nums = [int(i) for i in input().split()]

for j in range(len(nums)):
    for i in range(len(nums)-1):
        if nums[i+1] < nums[i]:
            nums[i+1], nums[i] = nums[i], nums[i+1]
print(*nums)