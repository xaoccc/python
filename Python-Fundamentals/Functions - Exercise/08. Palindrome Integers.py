def palidrome():
    nums_input = input().split()
    reversed_second_half = reversed(nums_input[len(nums_input) // 2 : len(nums_input)])
    reversed_second_half_list = []
    
    for i in reversed_second_half:
        reversed_second_half_list.append(int(i))
    
    print(reversed_second_half_list)

palidrome()
