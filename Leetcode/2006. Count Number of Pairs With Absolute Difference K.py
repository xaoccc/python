class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result = [ k for i in nums for j in nums if i - j == k]
        return len(result)
