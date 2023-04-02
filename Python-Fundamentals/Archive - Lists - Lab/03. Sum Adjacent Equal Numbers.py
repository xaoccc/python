nums = [int(i) for i in input().split()]
for i in range(1, len(nums) - 1):
    if nums[i] == nums[i - 1]:
        nums[i] *= 2
        nums.pop(i-1)
for i in range(1, len(nums) - 1):
    if nums[i] == nums[i - 1]:
        nums[i] *= 2
        nums.pop(i-1)
for i in range(1, len(nums) - 1):
    if nums[i] == nums[i - 1]:
        nums[i] *= 2
        nums.pop(i-1)

print(*nums)