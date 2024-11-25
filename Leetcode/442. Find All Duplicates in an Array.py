class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        my_dict = {}
        result = []
        for item in nums:
            if item in my_dict and item not in result:
                result.append(item)
            my_dict[item] = True
        return result