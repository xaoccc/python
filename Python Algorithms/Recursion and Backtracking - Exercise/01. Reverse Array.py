elements = input().split()

if len(elements) == 1:
    print(elements[0])

else:
    def reverse_array(idx, elements):
        if idx <= (len(elements) // 2) - 1:
            swap_idx = len(elements) - 1 - idx
            elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
            reverse_array(idx + 1, elements)
        if idx == (len(elements) // 2) - 1:
            print(" ".join(elements))

    reverse_array(0, elements)


# elements = input().split()
#
# def swap(idx, elements):
#     if len(elements) == 1:
#         return elements[idx]
#     if idx < (len(elements) // 2) - 1:
#         swap_idx = len(elements) - 1 - idx
#         elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
#         swap(idx + 1, elements)
#     else:
#         return
#
# swap(0, elements)
#
# print(" ".join(elements))