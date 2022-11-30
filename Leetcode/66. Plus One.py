class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if len(digits) > 1:       
            if digits[-1] == 9:
                for i in range(len(digits) - 1, -1, -1):
                    if digits[i] != 9:
                        digits[i] += 1
                        break
                    for j in range(0, i + 1):
 
                        if digits[i-j] == 9:
                            digits[i-j] = 0
                        if j == i:
                            digits[0] = 1
                            digits.append(0)
                        else:
                            break
                return digits
        if digits[-1] == 9:
            return [1,0]
        else:
            digits[-1] += 1
            return digits
