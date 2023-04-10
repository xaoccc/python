nums = [int(i) for i in input().split()]
result = [0] * len(nums)

for i in range(len(nums)):
    result[i] = min(nums)
    nums.remove(min(nums))
print(*result)