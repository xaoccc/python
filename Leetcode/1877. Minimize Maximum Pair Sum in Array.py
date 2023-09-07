class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nums_l = len(nums) // 2
        result = -1000

        for i in range(nums_l):
            current = nums[nums_l + i] + nums[nums_l - i - 1]
            if current > result:
                result = current

        return result
