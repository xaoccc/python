# Here min_idx is the index of the smallest number in the list. 
# At the beginning we assume, the current number (nums[idx]) is the smallest one.
for idx in range(len(nums)):
    min_idx = idx
    # Here we make sure we assume correct, as we check if any if the remaining numbers in the list is smaller
    # If it is smaller, we take its index
    for curr_idx in range(idx + 1, len(nums)):
        if nums[curr_idx] < nums[min_idx]:
            min_idx = curr_idx
    # We swap the two numbers. If they are the same index, no change will happen.
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]





# nums = [int(i) for i in input().split()]
# result = [0] * len(nums)

# for i in range(len(nums)):
#     result[i] = min(nums)
#     nums.remove(min(nums))
# print(*result)
