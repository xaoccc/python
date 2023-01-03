nums = input()
nums = nums.split(", ")
for i in range(len(nums)):
    if nums[i] == "0":
        nums.append(nums[i])
        nums.remove(nums[i])
for j in range(len(nums)):
    nums[j] = int(nums[j])
print(nums)
