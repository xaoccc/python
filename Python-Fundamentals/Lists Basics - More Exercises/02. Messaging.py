nums = input()
nums = nums.split(" ")
message = input()
final_message = ""
for i in range(len(nums)):
    index_num = 0
    for j in range(len(nums[i])):
        index_num += int(nums[i][j])
    if index_num >= len(nums):
        while index_num >= len(message):
            index_num -= len(message)
    final_message += message[index_num]
    message = message[0 : index_num : ] + message[index_num + 1 : : ]
print(final_message)
