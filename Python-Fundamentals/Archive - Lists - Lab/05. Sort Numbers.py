nums = [float(item) for item in input().split()]

nums = sorted(nums)
nums = [str(i) for i in nums]
" <= ".join(nums)
print(*nums)
