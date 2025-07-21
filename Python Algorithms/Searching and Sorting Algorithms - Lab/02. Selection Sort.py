# Here min_idx is the index of the smallest number in the list. 
# At the beginning we assume, the current number (nums[idx]) is the smallest one.
def selection_sort(nums):
    if not isinstance(nums, list):
        return "Invalid nums data type!"
    for idx in range(len(nums)):
        min_idx = idx
        # Compare the nums[idx] with the smallest of the remaining ones
        for curr_idx in range(idx + 1, len(nums)):
            if nums[curr_idx] < nums[min_idx]:
                min_idx = curr_idx
        # We swap the two numbers. If they are the same index, no change will happen.
        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
    return nums


print(selection_sort([51, 21, 16, 35, 84, 2, 11]))
