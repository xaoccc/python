class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits_product = 1
        digits_sum = 0
        n= str(n)        
        for i in range(len(n)):            
            digits_product *= int(n[i])
            digits_sum += int(n[i])
        return digits_product - digits_sum
