class Solution(object):
    def countPairs(self, nums, k):
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j > i and nums[i] == nums[j] and (i * j)  % k == 0:
                    count += 1
        return count
