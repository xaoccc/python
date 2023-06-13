class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            
            sub_array = sorted(nums[l[i] : r[i] + 1])
            diff = sub_array[1] - sub_array[0]
            for j in range(1, len(sub_array) - 1):
                if sub_array[j + 1] - sub_array[j] != diff:
                    result.append(False)
                    break
            
            else:
                result.append(True)
        return result
