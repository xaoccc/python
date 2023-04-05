nums = [int(i) for i in input().split()]
bomb = [int(i) for i in input().split()]

if bomb[0] in nums:
    while True:
        bomb_index = nums.index(bomb[0])
        start = bomb_index - bomb[1]
        end = bomb_index + bomb[1]
        if start < 0:
            start = 0
        if end >= len(nums):
            end = len(nums)
        nums = nums[:start] + nums[end+1:]
        if nums.count(bomb[0]) == 0:
            break
print(sum(nums))
