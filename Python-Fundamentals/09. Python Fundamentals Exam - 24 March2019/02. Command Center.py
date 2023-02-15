nums_list = [int(i) for i in input().split()]
command = input()
valid_num = 0

while command != "end":
    div_result = []
    command = command.split()
    
    if command[0] == "swap":
        if 0 <= int(command[1]) < len(nums_list) and 0 <= int(command[2]) < len(nums_list):
            nums_list[int(command[1])], nums_list[int(command[2])] = nums_list[int(command[2])], nums_list[int(command[1])]
            valid_num += 1
            print(nums_list)
        else:
            valid_num += 1
            print(nums_list)

    elif command[0] == "enumerate_list":
        valid_num += 1
        print(list(enumerate(nums_list)))
        
    elif command[0] == "max":
        valid_num += 1
        print(max(nums_list))
    
    elif command[0] == "min":
        valid_num += 1
        print(min(nums_list))
    
    elif command[0] == "get_divisible":
        for i in range(len(nums_list)):
            if nums_list[i] % int(command[2]) == 0:
                div_result.append(nums_list[i])
        valid_num += 1
        print(div_result)
        
    command = input()
print(valid_num)
