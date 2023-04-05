nums = [int(i) for i in input().split()]
operations = [int(i) for i in input().split()]
if operations[1] >= operations[0]:
    print("NO!")
else:
    nums = nums[operations[1]:operations[0]]
    if operations[2] in nums:
        print("YES!")
    else:
        print("NO!")
