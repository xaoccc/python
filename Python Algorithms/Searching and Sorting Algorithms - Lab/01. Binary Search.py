# binary search
def binary_search(elements, target):
    left = 0
    right = len(elements) - 1

    while right >= left:
        mid_index = (right - left) // 2

        if elements[mid_index] == target:
            return mid_index
        elif target < elements[mid_index]:
            right = mid_index - 1
        else:
            left = mid_index + 1
    return -1


elements = [int(i) for i in input().split()]
target = int(input())

print(binary_search(elements, target))

# linear search:
#
# elements = input().split()
# target = input()
# if target in elements:
#     print(elements.index(target))
# else:
#     print("-1")