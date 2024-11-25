class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}
        for i in s:
            if i not in my_dict:
                my_dict[i] = 0
            my_dict[i] += 1
        for j in range(len(s)):
            if my_dict[s[j]] == 1:
                return j
        return -1
