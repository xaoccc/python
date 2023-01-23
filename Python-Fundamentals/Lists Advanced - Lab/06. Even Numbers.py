nums = input().split(", ")
even_nums_i = []
for i in range(len(nums)):
    if int(nums[i]) % 2 == 0:
        even_nums_i.append(i)
print(even_nums_i)
