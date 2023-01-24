nums_list = input().split()
nums_list = [int(i) for i in nums_list]

command = input()
while command != "end":
    command = command.split()
    if command[0] == "swap":
        nums_list[int(command[1])], nums_list[int(command[2])] = nums_list[int(command[2])], nums_list[int(command[1])]
    elif command[0] == "multiply":
        nums_list[int(command[1])] = nums_list[int(command[1])] * nums_list[int(command[2])]
    elif command[0] == "decrease":
        for i in range(len(nums_list)):
            nums_list[i] -= 1
    command = input()
    
nums_list = [str(i) for i in nums_list]
print(", ".join(nums_list))
