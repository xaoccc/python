nums = input()

while nums != "stop playing":
    unique = True
    nums = [int(i) for i in nums.split()]
    for i in range(len(nums)):
        if nums.count(nums[i]) > 1:
            unique = False
    if not unique:
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums[i] += 3
    if unique:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] += 2
    sum_nums = sum(nums)
    nums = [str(i) for i in sorted(nums)]
    if unique:
        print(f"Unique list: {','.join(nums)}\nOutput: {sum_nums / len(nums):.2f}")
    else:
        print(f"Non-unique list: {':'.join(nums)}\nOutput: {sum_nums / len(nums):.2f}")
    nums = input()
