def str_to_int(nums_list = input()):
    nums_list = nums_list.split()
    int_list = list(map(int, nums_list))
    print(int_list)
str_to_int()
