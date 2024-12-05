def selection_sort(nums):

    for i in range(len(nums) - 1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if i != min_idx:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

    




print(selection_sort([4,2,6,5,1,3]))

 

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

