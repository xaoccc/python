class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        sum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                        sum += 1
        return sum
