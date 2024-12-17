def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, start, end):
    pivot = my_list[start]
    swap_index = start

    for i in range(start+1, end+1):
        # When pivot is greater than the current element, we swap the current element with the element at swap_index
        if pivot > my_list[i]:
            swap_index += 1
            swap(my_list, swap_index, i)
    
    swap(my_list, start, swap_index)
    return swap_index




my_list = [4,6,1,7,3,2,5]

print('List before running pivot():')
print(my_list)

returned_pivot_index = pivot(my_list, 0, 6)

print('\nList after running pivot():')
print(my_list)

print('\nPivot Index:')
print(returned_pivot_index)



"""
    EXPECTED OUTPUT:
    ----------------
    List before running pivot():
    [4, 6, 1, 7, 3, 2, 5]

    List after running pivot():
    [2, 1, 3, 4, 6, 7, 5]

    Pivot Index:
    3

 """