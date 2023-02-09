class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        list_ = []
        for i in range(len(s)):
            if i % 2 == 0:
                list_.append(s[i].count("*"))
        return sum(list_)
