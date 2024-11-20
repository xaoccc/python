class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        else:
            result = ""
            for i in range(0, len(s), k * 2):
                result += (s[i:i+k][::-1]+s[i+k:i+2*k])
            return result