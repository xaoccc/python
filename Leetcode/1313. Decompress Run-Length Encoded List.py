class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = [] 
        for i in range(0, len(nums), 2):
            sublist = []
            for j in range(nums[i]):
                sublist.append(nums[i+1])
            decompressed.extend(sublist)
        return decompressed
