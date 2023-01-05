nums_input = input()
nums_input = [eval(i) for i in nums_input.split(" ")]
command_input = input()
exchange_list = []
min_odd, min_even = 10000000, 10000000
min_odd_index, max_odd_index, max_even_index, min_even_index = 0, 0, 0, 0
max_odd, max_even = -10000000, -10000000
first_even, first_odd, last_even, last_odd = [], [], [], []

while command_input != "end":
    command_input = command_input.split(" ")
    if command_input[0] == "exchange":
        if 0 <= int(command_input[1]) < len(nums_input):
            exchange_list = nums_input[int(command_input[1]) + 1 : ] + nums_input[0 : int(command_input[1]) + 1]
            print(exchange_list)
        else:
            print("Invalid index")
    elif command_input[0] == "min":
        if command_input[1] == "odd":
            for i in range(len(nums_input)):
                if nums_input[i] <= min_odd and nums_input[i] % 2 == 1:
                    min_odd = nums_input[i]
                    min_odd_index = i
            if min_odd != 10000000:
                print(min_odd_index)
            else:
                print("No matches")
            
        elif command_input[1] == "even":
            for i in range(len(nums_input)):
                if nums_input[i] <= min_even and nums_input[i] % 2 == 0:
                    min_even = nums_input[i]
                    min_even_index = i
            if min_even != 10000000:
                print(min_even_index)
            else:
                print("No matches")
        
    elif command_input[0] == "max":
        if command_input[1] == "odd":
            for i in range(len(nums_input)):
                if nums_input[i] >= max_odd and nums_input[i] % 2 == 1:
                    max_odd = nums_input[i]
                    max_odd_index = i
            if max_odd != 10000000:
                print(max_odd_index)
            else:
                print("No matches")
            
        elif command_input[1] == "even":
            for i in range(len(nums_input)):
                if nums_input[i] >= max_even and nums_input[i] % 2 == 0:
                    max_even = nums_input[i]
                    max_even_index = i
            if max_even != 10000000:
                print(max_even_index)
            else:
                print("No matches")
            
    elif command_input[0] == "first":
        if command_input[2] == "odd":
            if len(nums_input) < int(command_input[1]):
                print("Invalid count")
            else:
                for i in range(len(nums_input)):
                    if nums_input[i] % 2 == 1:
                        first_odd.append(nums_input[i])
                if len(first_odd) > int(command_input[1]):
                    first_odd = first_odd[0 : int(command_input[1])]
                print(first_odd)
                
        elif command_input[2] == "even":
            if len(nums_input) < int(command_input[1]):
                print("Invalid count")
            else:
                for i in range(len(nums_input)):
                    if nums_input[i] % 2 == 0:
                        first_even.append(nums_input[i])
                if len(first_even) > int(command_input[1]):
                    first_even = first_even[0 : int(command_input[1])]
                print(first_even)
                
        
    elif command_input[0] == "last":
        if command_input[2] == "odd":
            if len(nums_input) < int(command_input[1]):
                print("Invalid count")
            else:
                for i in range(len(nums_input) - 1, -1, -1):
                    if nums_input[i] % 2 == 1:
                        last_odd.append(nums_input[i])
                if len(last_odd) > int(command_input[1]):
                    last_odd = last_odd[0 : int(command_input[1])]
                last_odd.reverse()
                print(last_odd)
                
        elif command_input[2] == "even":
            if len(nums_input) < int(command_input[1]):
                print("Invalid count")
            else:
                for i in range(len(nums_input) - 1, -1, -1):
                    if nums_input[i] % 2 == 0:
                        last_even.append(nums_input[i])
                if len(last_even) > int(command_input[1]):
                    last_even = last_even[0 : int(command_input[1])]
                last_even.reverse()
                print(last_even)
    
    command_input = input()
