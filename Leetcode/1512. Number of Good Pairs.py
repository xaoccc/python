class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs_num = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                 if nums[i] == nums[j] and i < j:
                        good_pairs_num += 1
        return good_pairs_num
