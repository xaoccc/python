class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        sorted_list = sorted(s)
        for i in range(len(s)):
            sorted_list[i] = sorted_list[i][1: ]
            sorted_list[i] = sorted_list[i][::-1]
        return " ".join(sorted_list)
