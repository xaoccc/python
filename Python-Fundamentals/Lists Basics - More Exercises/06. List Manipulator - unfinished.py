nums_input = input().split()
nums_input = [eval(i) for i in nums_input]
new_list = []
max_even, max_odd, min_even, min_odd = -10000000, -10000000, 10000000, 10000000
max_even_index, max_odd_index, min_even_index, min_odd_index = 0, 0, 0, 0

while True:
    command = input()
    command = command.split()
    print
    if command[0] == "end":
        break
    elif command[0] == "exchange":
        print(nums_input[int(command[1]) + 1: ] + nums_input[0 : int(command[1]) + 1])
    elif command == ["max", "even"]:
        for i in range(len(nums_input) -1, -1, -1):
            if nums_input[i] > max_even and nums_input[i] % 2 == 0:
                max_even = nums_input[i]
                max_even_index = i
        print(max_even_index)
    elif command == ["max", "odd"]:
        for j in range(len(nums_input) -1, -1, -1):
            if nums_input[j] > max_odd and nums_input[j] % 2 != 0:
                max_odd = nums_input[j]
                max_odd_index = j
        print(max_odd_index)
        
    elif command == ["min", "even"]:
        for k in range(len(nums_input) -1, -1, -1):
            if nums_input[k] < min_even and nums_input[k] % 2 == 0:
                min_even = nums_input[k]
                min_even_index = k
        print(min_even_index)
    elif command == ["min", "odd"]:
        for l in range(len(nums_input) -1, -1, -1):
            if nums_input[l] < min_odd and nums_input[l] % 2 != 0:
                min_odd = nums_input[l]
                min_odd_index = l
        if min_odd_index == 0 and min_odd_index % 2 == 0:
            print("No matches")
        else:
            print(min_odd_index)
