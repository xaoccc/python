class Solution(object):
    def maxProduct(self, nums):
        return (sorted(nums)[-1] - 1) * (sorted(nums)[-2] -1)
