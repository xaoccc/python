nums = [int(i) for i in input().split() if int(i) > -1]
if len(nums) == 0:
    print("empty")
else:
    nums = reversed([str(i) for i in nums])
    print(" ".join(nums))
