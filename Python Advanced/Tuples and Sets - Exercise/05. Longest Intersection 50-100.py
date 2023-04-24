rows = int(input())
max_len = 0
longest = []
min_num, max_num = None, None

for i in range(rows):
    nums = input().split("-")
    pair_one = tuple(map(int, nums[0].split(",")))
    pair_two = tuple(map(int, nums[1].split(",")))
    intersection = min([pair_two[1] - pair_one[0], pair_one[1] - pair_two[0]])
    if intersection + 1 > max_len:
        max_len = intersection + 1
        if pair_two[1] - pair_one[0] == max_len - 1:
            min_num = pair_one[0]
            max_num = pair_two[1]
        elif pair_one[1] - pair_two[0] == max_len - 1:
            min_num = pair_two[0]
            max_num = pair_one[1]
if min_num and max_num:
    for i in range(min_num, max_num + 1):
        longest.append(i)
print(f"Longest intersection is {longest} with length {max_len}")
