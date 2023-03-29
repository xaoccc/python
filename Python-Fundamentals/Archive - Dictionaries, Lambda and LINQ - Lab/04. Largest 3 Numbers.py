nums = [int(i) for i in input().split()]
print(*(sorted(nums)[::-1][:3]))
