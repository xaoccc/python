class Solution(object):
    def separateDigits(self, nums):
        nums = [str(i) for i in nums]
        result = []
        for i in range(len(nums)):
            if len(nums[i]) > 1:
                list(nums[i])
                for j in range(len(nums[i])):
                    result.append(nums[i][j])
            else:
                result.append(nums[i])
        return [int(i) for i in result]
