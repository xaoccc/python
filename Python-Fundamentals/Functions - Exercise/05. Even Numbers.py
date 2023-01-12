def another_function(nums_list):
    nums_list = nums_list.split()
    new_list = []
    for i in range(len(nums_list)):
        if int(nums_list[i]) % 2 == 0:
            new_list.append(int(nums_list[i]))
    print(new_list)
another_function(input())
