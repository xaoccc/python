class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for i in patterns:
            if i in word:
                result += 1
        return result
