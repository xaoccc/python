nums = [int(i) for i in input().split()]

idx = 0
def sum_nums(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + sum_nums(nums, idx + 1)
    
print(sum_nums(nums, idx))
