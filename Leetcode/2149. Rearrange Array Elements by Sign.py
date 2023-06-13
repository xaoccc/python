class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = list(filter(lambda x: x>0, nums))
        neg = list(filter(lambda x: x<0, nums))
        result = []
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        
        return result
