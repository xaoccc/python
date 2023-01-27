#The input is a string, so we convert it to a list, then convert the elements of the list into int.
nums_input = input().split()
nums_input = list(map(int, nums_input))

while True:
    #Create 12 variables inside the loop, so we have them like that for each command check - 4 for the numbers, 4 for the lists and 4 for the indexes
    max_even, max_odd, min_even, min_odd = -10000000, -10000000, 10000000, 10000000
    first_even, first_odd, last_even, last_odd = [], [], [], []
    max_even_index, max_odd_index, min_even_index, min_odd_index = 0, 0, 0, 0
    #On each iteration the command is converted into a list, so we can make all checks
    command = input().split()

    #The first check is the breakpoint and is right after the command. The output is also here.
    if command[0] == "end":
        print(nums_input)
        break
        
    #The second check is for the command "exchange". First we have to check if the index in the command valid.
    elif command[0] == "exchange":
        if int(command[1]) >= len(nums_input) or int(command[1]) < 0:
            print("Invalid index")
        #If the index is valid, we go here and exchange the places of the two parts of the list - before and after the index.
        else:
            nums_input = nums_input[int(command[1]) + 1: ] + nums_input[0 : int(command[1]) + 1]
    
    #The third check is for the biggest even/odd number.
    elif command[0] == "max":
        if command[1] == "even":
            #The tricky part is the condition "If there are two or more equal min/max elements, return the index of the rightmost one"
            #This is the reason we loop the list backwards.
            for i in range(len(nums_input) - 1, - 1, - 1):
                #We check for two conditions at a time - the number must be even and at the same time greater than our initially created variable, if such number is found, 
                #we check the next one with it and so on, until the end of the list.
                if nums_input[i] > max_even and nums_input[i] % 2 == 0:
                    max_even = nums_input[i]
                    max_even_index = i
            #If the biggest number is exactly as our variable, which we chose to be the smallest number(we could use a way smaller number, of course),
            #apparently there are no matches in the criteria, so we get an output "No matches"
            if max_even == -10000000:
                print("No matches")
            else:
                print(max_even_index)
                
        else:
            #We use the same logic for the odd numbers:
            for i in range(len(nums_input) -1, -1, -1):
                if nums_input[i] > max_odd and nums_input[i] % 2 != 0:
                    max_odd = nums_input[i]
                    max_odd_index = i
            if max_odd == -10000000:
                print("No matches")
            else:
                print(max_odd_index)
    
    #The fourth check is for the smallest even/odd number. We use the same logic as for the previuos check.
    elif command[0] == "min":
        if command[1] == "even":
            for i in range(len(nums_input) -1, -1, -1):
                if nums_input[i] < min_even and nums_input[i] % 2 == 0:
                    min_even = nums_input[i]
                    min_even_index = i
            if min_even == 10000000:
                print("No matches")
            else:
                print(min_even_index)                
        else:
            for i in range(len(nums_input) -1, -1, -1):
                if nums_input[i] < min_odd and nums_input[i] % 2 != 0:
                    min_odd = nums_input[i]
                    min_odd_index = i
            if min_odd == 10000000:
                print("No matches")
            else:
                print(min_odd_index)
                
    #The fifth check is about creating a list with the first even/odd numbers        
    elif command[0] == "first":
        #If the command is trying to check for more numbers than we have in the list, the program will print an error message "Invalid count"
        if int(command[1]) > len(nums_input):
            print("Invalid count")
        #If the command is valid, we go here:
        else:
            if command[2] == "even":
                #For each even number we find in the list, we take it and put it inside the new list we've already created, until we reach the written in the command
                #number of even numbers 
                for i in range(len(nums_input)):
                    if nums_input[i] % 2 == 0:
                        first_even.append(nums_input[i])
                    if len(first_even) == int(command[1]):
                        break
                print(first_even)
            elif command[2] == "odd":
                #For the odd numbers we use the same logic as for the even
                for i in range(len(nums_input)):
                    if nums_input[i] % 2 != 0:
                        first_odd.append(nums_input[i])
                    if len(first_odd) == int(command[1]):
                        break
                print(first_odd)
                
    #The last command is tricky. We have to take the last even/odd numbers and put them into a list.
    elif command[0] == "last":
        #First we validate the command. We cannot have a greater number than the number of elements in the list.
        if int(command[1]) > len(nums_input):
            print("Invalid count")
        else:
            if command[2] == "even":
                #The command is valid, so we start iterating from the end of the list to the beginning:
                for i in range(len(nums_input) - 1, -1, -1):
                    if nums_input[i] % 2 == 0:
                        last_even.append(nums_input[i])
                    if len(last_even) == int(command[1]):
                        break
                #The list with the last even numbers, as you can imagine, is backwards, so we have to make it look properly, so we reverse it and print it:
                last_even.reverse()
                print(last_even)
            elif command[2] == "odd":
                #For the odd numbers list we use the same logic as for the even ones.
                for i in range(len(nums_input) - 1, -1, -1):
                    if nums_input[i] % 2 != 0:
                        last_odd.append(nums_input[i])
                    if len(last_odd) == int(command[1]):
                        break
                last_odd.reverse()
                print(last_odd)
