nums = sorted(float(i) for i in input().split())
for i in range(0, len(nums)):
    if i == 0:
        if nums[i].is_integer():
            print(f"{nums[i]:.0f} -> {nums.count(nums[i])}")
        else:
            print(f"{nums[i]} -> {nums.count(nums[i])}")
        
    if i > 0 and nums[i] != nums[i-1]:
        if nums[i].is_integer():
            print(f"{nums[i]:.0f} -> {nums.count(nums[i])}")
        else:
            print(f"{nums[i]} -> {nums.count(nums[i])}")
