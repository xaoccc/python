
def quicksort(start, end, nums):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] <= nums[pivot]:
            left += 1

        if nums[right] >= nums[pivot]:
            right -= 1
    nums[pivot], nums[right] = nums[right], nums[pivot]
    quicksort(start, right - 1, nums)
    quicksort(left, end, nums)
    return nums

nums = [int(i) for i in input().split()]

print(*quicksort(0, len(nums)-1, nums))