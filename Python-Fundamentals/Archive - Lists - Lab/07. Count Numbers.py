nums = [int(i) for i in input().split()]

nums = sorted(nums)

for i in sorted(set(nums)):
    print(f"{i} -> {nums.count(i)}")
