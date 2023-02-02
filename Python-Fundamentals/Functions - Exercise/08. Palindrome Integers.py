def palidrome(nums_input):
  
    #We have to check each number from the list if it is a palidrome number (as string)
    for num in range(len(nums_input)):
        #We have to divide the string number in two halves and compare them. That is why we create a variable for the second half
        reversed_second_half_str = ""
        #We have two options - even or odd LENGHT of the number. For each of them we have a different second half
        if len(nums_input[num]) % 2 == 0:
            reversed_second_half = reversed(nums_input[num][len(nums_input[num]) // 2 : len(nums_input[num])])
        else:
            reversed_second_half = reversed(nums_input[num][(len(nums_input[num]) // 2) + 1 : len(nums_input[num])])
        for i in reversed_second_half:
            reversed_second_half_str += i
            
        #The first half is easy - we take the first half of the string
        first_half = nums_input[num][0 : len(nums_input[num]) // 2]
    
        #We compare the first and the secound half and print the output
        if first_half == reversed_second_half_str:
            print(True)
        else:
            print(False)
            
#Now we can call the function whenever we want :)
palidrome(input().split(", "))
