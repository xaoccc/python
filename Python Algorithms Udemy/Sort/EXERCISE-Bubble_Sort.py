def bubble_sort(nums):
    # Two pointers - one start to end and one end ot start comparing the values and switch if not in the correct sort(left to right)
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums





print(bubble_sort([1, 2, 300, 44, 5, 34, 345, 4534, 43, 12, 16, 142, 87, 7]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 300, 44, 5, 34, 345, 4534, 43, 12, 16, 142, 87, 7]
 """