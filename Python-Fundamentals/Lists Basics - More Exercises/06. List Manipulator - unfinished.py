nums_input = input().split()
nums_input = list(map(int, nums_input))
first_even, first_odd, last_even, last_odd = [], [], [], []
max_even_index, max_odd_index, min_even_index, min_odd_index = 0, 0, 0, 0
exchange = 0

while True:
    max_even, max_odd, min_even, min_odd = -2 ** 32, -2 ** 32, 2 ** 32, 2 ** 32
    command = input().split()

    if command[0] == "end":
        if exchange > 0:
            print(nums_input)
        break
    elif command[0] == "exchange":
        if int(command[1]) > len(nums_input) - 1:
            print("Invalid index")
        else:
            nums_input = nums_input[int(command[1]) + 1:] + nums_input[0 : int(command[1]) + 1]
            exchange += 1
    elif command == ["max", "even"]:
        for i in range(len(nums_input) - 1, - 1, - 1):
            if nums_input[i] > max_even and nums_input[i] % 2 == 0:
                max_even = nums_input[i]
                max_even_index = i
        if max_even == -2 ** 32:
            print("No matches")
        else:
            print(max_even_index)
    elif command == ["max", "odd"]:
        for j in range(len(nums_input) -1, -1, -1):
            if nums_input[j] > max_odd and nums_input[j] % 2 != 0:
                max_odd = nums_input[j]
                max_odd_index = j
        if max_odd == -2 ** 32:
            print("No matches")
        else:
            print(max_odd_index)
        
    elif command == ["min", "even"]:
        for k in range(len(nums_input) -1, -1, -1):
            if nums_input[k] < min_even and nums_input[k] % 2 == 0:
                min_even = nums_input[k]
                min_even_index = k
        if min_even == 2 ** 32:
            print("No matches")
        else:
            print(min_even_index)
    elif command == ["min", "odd"]:
        for l in range(len(nums_input) -1, -1, -1):
            if nums_input[l] < min_odd and nums_input[l] % 2 != 0:
                min_odd = nums_input[l]
                min_odd_index = l
        if min_odd == 2 ** 32:
            print("No matches")
        else:
            print(min_odd_index)
    elif command[0] == "first":
        if int(command[1]) > len(nums_input):
            print("Invalid count")
        else:
            if command[2] == "even":
                for m in range(len(nums_input)):
                    if nums_input[m] % 2 == 0:
                        first_even.append(nums_input[m])
                    if len(first_even) == int(command[1]):
                        break
                print(first_even)
            elif command[2] == "odd":
                for n in range(len(nums_input)):
                    if nums_input[n] % 2 != 0:
                        first_odd.append(nums_input[n])
                    if len(first_odd) == int(command[1]):
                        break
                print(first_odd)
    elif command[0] == "last":
        if int(command[1]) > len(nums_input):
            print("Invalid count")
        else:
            if command[2] == "even":
                for o in range(len(nums_input) - 1, -1, -1):
                    if nums_input[o] % 2 == 0:
                        last_even.append(nums_input[o])
                    if len(last_even) == int(command[1]):
                        break
                last_even.reverse()
                print(last_even)
            elif command[2] == "odd":
                for p in range(len(nums_input) - 1, -1, -1):
                    if nums_input[p] % 2 != 0:
                        last_odd.append(nums_input[p])
                    if len(last_odd) == int(command[1]):
                        break
                last_odd.reverse()
                print(last_odd)
