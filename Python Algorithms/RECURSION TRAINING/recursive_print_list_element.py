# print list 1ith one element less each time:
def recursive_print_list_element(nums, i):


    if i == len(nums) + 1:
        return
    recursive_print_list_element(nums, i + 1)
    print(nums[:i])

recursive_print_list_element(input().split(), 1)


# print list elements from last to first
def recursive_print_list_element(nums, i):

    if i == len(nums):
        return
    recursive_print_list_element(nums, i + 1)
    print(nums[i])

recursive_print_list_element(input().split(), 0)


# print list elements from first to last
def recursive_print_list_element(nums, i):

    if i == len(nums) + 1:
        return
    recursive_print_list_element(nums, i + 1)
    print(nums[len(nums) - i])

recursive_print_list_element(input().split(), 1)
