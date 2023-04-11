def merge_lists(left, right):
    # Create an empty list with number of elements equal to the sum of both halves - left and right
    result = [None] * (len(left) + len(right))
    left_idx = 0
    right_idx = 0
    result_idx = 0
    # First loop is sorting both left and right list elements
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] >= right[right_idx]:
            result[result_idx] = right[right_idx]
            right_idx += 1
        else:
            result[result_idx] = left[left_idx]
            left_idx += 1
        result_idx += 1
    # These 2 loops are checking if there are any unused elements in some of the lists (left and right)
    # Note that there are always some and we don't want some of the elements of result list to be None type.
    # So we must fill all spaces of result before returning it
    while left_idx < len(left):
        result[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1
    while right_idx < len(right):
        result[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    return result

def merge_sort(nums):
    # The terminating point is where the list has only one element
    if len(nums) == 1:
        return nums
    # We divide the list into 2 sublists
    left = nums[:len(nums) // 2]
    right = nums[len(nums) // 2:]

    return merge_lists(merge_sort(left), merge_sort(right))

# User input
nums = [int(i) for i in input().split()]

print(*merge_sort(nums))