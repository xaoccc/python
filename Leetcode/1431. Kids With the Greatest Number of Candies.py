class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []        
        for i in range(len(candies)):
            output.append(candies[i] + extraCandies >= max(candies))
        return output
