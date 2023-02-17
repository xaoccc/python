class Solution:
    def replaceDigits(self, s: str) -> str:
        for i in range(len(s)):
            if s[i].isdigit():
                s = s[:i] + chr(ord(s[i-1])+int(s[i])) + s[i+1:]
        return s
