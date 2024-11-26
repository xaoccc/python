# O(nlogn)
# def longest_consecutive_sequence(input):
#     if not input:
#         return 0
#     input = sorted(set(input))
#     lengths = [1]
#     for i in range(0, len(input)-1):
#         if input[i] + 1 == input[i + 1]:
#             if lengths[-1] > 0:
#                 lengths[-1] += 1
#             else:
#                 lengths[-1] += 2
#         else:
#             lengths.append(1)
#
#     return max(lengths)

# O(n)
def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting if it's the start of a sequence
        if num - 1 not in num_set:
            length = 1
            current_num = num

            while current_num + 1 in num_set:
                current_num += 1
                length += 1

            longest = max(longest, length)

    return longest



print( longest_consecutive_sequence([100, 200, 300, 301]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""