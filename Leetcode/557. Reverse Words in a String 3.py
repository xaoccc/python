class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        new_list = []
        for i in range(len(s)):
            new_list.append(s[i][::-1])
        return " ".join(new_list)
