class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        if len(nums) < 2:
            return [0]
        else:
            leftSum = [0, nums[0]]
            for i in range(2, len(nums)):
                leftSum.append(sum(nums[:i]))
                    
            rightSum = [nums[-1], 0]        
            for i in range(0, len(nums)-2):        
                rightSum.insert(i, sum(nums[i+1:]))    

            for i in range(len(nums)):
                result[i] = abs(leftSum[i] - rightSum[i])
                
            return result
