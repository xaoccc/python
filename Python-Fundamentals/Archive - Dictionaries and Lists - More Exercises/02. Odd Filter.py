nums = [int(i) for i in input().split() if int(i) % 2 == 0]
average = sum(nums) // len(nums)
result = [i + 1 if i > average else i - 1 for i in nums]
print(*result)
