import time
start = time.time()
nums = [int(i) for i in input().split()]
target = int(input())
i = 0

while True:
    j = i + 1
    while True:
        found = False
        if nums[i] + nums[j] == target and i != j:
            print(f"{nums[i]} + {nums[j]} = {target}")
            nums.pop(max([i, j]))
            nums.pop(min([i, j]))
            found = True
            j = i
        if j == len(nums) - 1 or i >= len(nums):
            break
        if not found:
            j += 1
    if i >= len(nums) - 1:
        break
    i += 1
end = time.time()
print(f"Total time:{end - start}")
