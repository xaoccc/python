def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while temp < nums[j] and j > -1:
            nums[j + 1] = nums[j]
            nums[j] = temp
            j -= 1

    return nums






print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """

