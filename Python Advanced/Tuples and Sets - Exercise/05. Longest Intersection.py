rows = int(input())
max_len = 0
longest = []
min_num, max_num = None, None

for i in range(rows):
    nums = input().split("-")
    pair_one = tuple(map(int, nums[0].split(",")))
    pair_two = tuple(map(int, nums[1].split(",")))
    if min(pair_one) > max(pair_two) or max(pair_one) < min(pair_two):
        continue
    if min(pair_one) == max(pair_two) or max(pair_one) == min(pair_two):
        min_num = max(pair_one[0], pair_two[0])
        max_num = min(pair_one[1], pair_two[1])
        if max_len < 1:
            max_len = 1
    else:
        intersection = min(pair_one[1], pair_two[1]) - max(pair_one[0], pair_two[0])
        if intersection > max_len:
            max_len = intersection + 1
            min_num = max(pair_one[0], pair_two[0])
            max_num = min(pair_one[1], pair_two[1])
        if intersection == max_len and max_len == 0:
            min_num = max(pair_one[0], pair_two[0])
            max_num = min(pair_one[1], pair_two[1])
            max_len = 1
            

if min_num != None and max_num != None:
    for i in range(min_num, max_num + 1):
        longest.append(i)
print(f"Longest intersection is {longest} with length {max_len}")


# longest = set()
# longest_intersection = 0
# for i in range(int(input())):
#     first, second = [el.split(",") for el in input().split("-")]
#     first_range = set(range(int(first[0]), int(first[1]) + 1))
#     second_range = set(range(int(second[0]), int(second[1]) + 1))
#     intersection = first_range.intersection(second_range)
#     if len(intersection) > len(longest):
#         longest = intersection
# print(f"Longest intersection is {list(longest)} with length {len(longest)}")
