class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:    
        output, j = [], 0
        while nums:
            nums_set = set(nums)
            output.append([])
            i = 0
            while nums_set:        
                current_num = nums[i]
                if current_num in nums_set:
                    output[j].append(current_num)
                    del nums[i]
                    nums_set.discard(current_num)
                else:
                    i += 1                
            j += 1
        return output
