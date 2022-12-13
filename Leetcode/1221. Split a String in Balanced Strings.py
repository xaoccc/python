class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_l = 0
        count_r = 0
        output = 0
        for i in range(len(s)):
            if s[i] == "R":
                count_r += 1
            if s[i] == "L":
                count_l += 1
            if count_r == count_l:
                output += 1
                count_l = 0
                count_r = 0        
        return output
