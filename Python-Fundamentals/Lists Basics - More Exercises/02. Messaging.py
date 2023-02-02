#We split the input into a list
nums = input().split(" ")
message = input()
#Here we will store the output
final_message = ""

#We iterate the list to find each index to get the message
for i in range(len(nums)):
    #Do not forget to start from 0 at each loop
    index_num = 0
    #The sum of the digits of each element is the index we should use in the "message" string, so we loop though each element of nums[] and sum the digits
    for j in range(len(nums[i])):
        index_num += int(nums[i][j])
    #Now that we have the index, we chech if it is not too long.
    if index_num >= len(nums):
        #If it is too long, we shorten it by the length of the "message" string, so we count over and over, until we have an index in range
        while index_num >= len(message):
            index_num -= len(message)
    #We have a valid index, so we get the corresponding letter and add it to the output:
    final_message += message[index_num]
    #Here we are slicing the string, thus removing the used index
    message = message[0 : index_num : ] + message[index_num + 1 : : ]
#After all elements of the list are checked, all indexes are found and all letters of the secret message are added, we print the secret message:
print(final_message)
