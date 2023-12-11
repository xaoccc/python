class Solution(object):
    def countPairs(self, nums, target):
        return len([target for j, num2 in enumerate(nums) for i, num1 in enumerate(nums) if i < j and num1 + num2 < target])