def max_min_sum():
    nums_input = input().split()
    for i in range(len(nums_input)):
        nums_input[i] = int(nums_input[i])
    print(f"The minimum number is {min(nums_input)}")
    print(f"The maximum number is {max(nums_input)}")
    print(f"The sum number is: {sum(nums_input)}")
max_min_sum()
