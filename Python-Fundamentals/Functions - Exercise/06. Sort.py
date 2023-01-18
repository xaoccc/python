def num_sort():
    nums_input = input().split()
    for i in range(len(nums_input)):
        nums_input[i] = int(nums_input[i])
    sorted_nums = sorted(nums_input)
    print(sorted_nums)
num_sort()
