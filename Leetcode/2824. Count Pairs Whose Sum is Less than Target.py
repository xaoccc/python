class Solution(object):
    def countPairs(self, nums, target):
        res = 0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i < j and num1 + num2 < target:
                    res += 1

        return res