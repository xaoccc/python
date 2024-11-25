# solution 1 using set()
# def item_in_common(list1, list2):
#     if len(set(list1 + list2)) != len(list1 + list2):
#         return True
#     return False

# solution 2 using dict()
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1,3,6]
list2 = [2,4,5]

print(item_in_common(list1, list2))

