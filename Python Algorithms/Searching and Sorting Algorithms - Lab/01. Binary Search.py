# Improved version of binary search
# - Data type validation
# - Empty list validation
# - Fixed bug with finding first and last elements
def index_binary_search(elements, target):

    if not isinstance(elements, list):
        return "Invalid elements data type!"
    if not isinstance(target, int):
        return "Invalid target data type!"
    if not elements:
        return -1
    left = 0
    right = len(elements) - 1

    while right >= left:
        mid_index = left + (right - left) // 2

        if elements[mid_index] == target:
            return mid_index
        elif target < elements[mid_index]:
            right = mid_index - 1
        else:
            left = mid_index + 1
    return -1


print(index_binary_search([1, 2, 3, 4, 5], 2))
