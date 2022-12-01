class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output_array = []
        j=0
        for i in range(2 * n):
            if i % 2 == 0 or i == 0:
                output_array.append(nums[i-j])
            else:                
                output_array.append(nums[n+j])
                j+=1
        return output_array
