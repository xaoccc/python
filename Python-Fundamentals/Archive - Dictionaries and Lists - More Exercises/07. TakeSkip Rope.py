hidden_message = input()
nums, non_nums, take_list, skip_list = [], [], [], []
message, sum_chars = "", 0
for char in hidden_message:
    if char.isdigit():
        nums.append(int(char))
    else:
        non_nums.append(char)
non_nums = "".join(non_nums)
for i in range(len(nums)):
    if i % 2 == 0:
        take_list.append(nums[i])
    else:
        skip_list.append(nums[i])
for i in range(len(nums) // 2):
    message += non_nums[sum_chars : take_list[i] + sum_chars]
    sum_chars += skip_list[i] + take_list[i]
print(message)
