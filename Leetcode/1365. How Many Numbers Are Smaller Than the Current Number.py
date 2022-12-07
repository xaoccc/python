class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller = []
        
        for i in range(len(nums)):
            smaller_num = 0
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    smaller_num += 1
            smaller.append(smaller_num)
        return smaller
