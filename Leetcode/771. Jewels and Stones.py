class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        output = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    output += 1
        return output
