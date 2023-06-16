nums = [int(i) for i in input().split()]
is_sorted = False
i = 0
while not is_sorted:
    # We create flag is_sorted, 
    # so until there are two neighbouring unsorted nums, the loop will continue
    is_sorted = True
    for j in range(1, len(nums) - i):
        if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            is_sorted = False
    # On each for loop, we find the biggest number and put it in the end
    # So we decrease the collection to check with 1 (because we have 1 number on correct position)
    # We do the same for all remaining numbers until they are sorted
    i += 1
print(*nums)


# nums = [int(i) for i in input().split()]

# for j in range(len(nums)):
#     for i in range(len(nums)-1):
#         if nums[i+1] < nums[i]:
#             nums[i+1], nums[i] = nums[i], nums[i+1]
# print(*nums)
