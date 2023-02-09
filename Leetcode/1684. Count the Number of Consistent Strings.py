class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:        
        success = 0
        for i in range(len(words)):
            count = 0
            for j in range(len(words[i])):
                if words[i][j] in allowed :
                    count += 1
                if j == len(words[i]) - 1 and count == len(words[i]):
                    success += 1
        return success
