def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1
              
    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


def merge_sort(nums):
    mid_idx = len(nums) // 2
    if mid_idx == 0:
        return nums
    left = merge_sort(nums[:mid_idx])
    right = merge_sort(nums[mid_idx:])

    return merge(left, right)



original_list = [3,1,5,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)



"""
    EXPECTED OUTPUT:
    ----------------
    Original List: [3, 1, 4, 2]

    Sorted List: [1, 2, 3, 4]

 """