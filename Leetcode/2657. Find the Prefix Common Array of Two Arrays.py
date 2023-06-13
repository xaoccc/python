class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        for i in range(1, len(A) + 1):
            result.append(len(set(A[:i]) & set(B[:i])))
        return result
