class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_nums, min_nums = [max(nums)], [min(nums)]
        nums.remove(max(nums))
        nums.remove(min(nums))
        max_nums.append(max(nums))
        min_nums.append(min(nums))

        return (max_nums[0] * max_nums[1]) - (min_nums[0] * min_nums[1])
