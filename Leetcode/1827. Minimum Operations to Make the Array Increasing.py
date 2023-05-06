class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(len(nums) - 1):

            if nums[i + 1] < nums[i]:
                operations += nums[i] - nums[i + 1] + 1
                nums[i + 1] += nums[i] - nums[i + 1] + 1
            elif nums[i + 1] == nums[i]: 
                operations += 1
                nums[i + 1] += 1
        return operations
