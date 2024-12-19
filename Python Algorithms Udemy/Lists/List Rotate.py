def rotate(nums, k):
    nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
    return nums

nums = [1, 2]
rotate(nums, 3)
print("Rotated array:", nums)

"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""