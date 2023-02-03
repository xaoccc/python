class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(arr)):
            for j in range(0, len(arr), 2):
                if i + j + 1 <= len(arr):
                    for k in range(len(arr[i:i+j+1])):
                        sum += arr[i:i+j+1][k]
        return sum
