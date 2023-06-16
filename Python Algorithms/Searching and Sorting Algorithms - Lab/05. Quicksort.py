
def quicksort(start, end, nums):
    if start >= end:
        return
    # We take the first number from the list
    pivot = start
    left = start + 1
    right = end

    # Here we sort the list in two parts - smaller or equal the pivot(first half) and bigger than the pivot (secon half) 
    while left <= right:
        # We swap the numbers, if we find smaller number in the second half:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] <= nums[pivot]:
            left += 1

        if nums[right] >= nums[pivot]:
            right -= 1
    # We move the current pivot after the list of smaller/equal nums, 
    # so in the worst case, the pivot will be equal to the biggest number in this sub-list, which is ok
    nums[pivot], nums[right] = nums[right], nums[pivot]

    # Do the same for the first half:
    quicksort(start, right - 1, nums)
    # Then for the second half
    quicksort(left, end, nums)
    return nums

nums = [int(i) for i in input().split()]

print(*quicksort(0, len(nums)-1, nums))
