class Solution:
    from math import floor
    def mySqrt(self, x: int) -> int:
        r = x
        #Here we decide how precise should be our result
        precision = 10 ** (-5)
    
        while abs(x - r * r) > precision:
            #This is the formula for finding sqrt, as we can set the precision rate(above). Add the approximate root (r) with the original number (x) divided by the approximate root and divide by 2. We do this until the difference in the approximate root along the iterations is less than the desired value (or precision value).
            r = (r + x / r) / 2
        
        return floor(r)
