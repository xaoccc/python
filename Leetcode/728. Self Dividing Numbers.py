class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for i in range(left, right + 1):
            if "0" in str(i):
                continue
            result.append(i)
            for j in range(len(str(i))):
                if i % int(str(i)[j]) != 0:
                    result.pop()
                    break
        return result
