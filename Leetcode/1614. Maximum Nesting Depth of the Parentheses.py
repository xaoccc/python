class Solution:
    def maxDepth(self, s: str) -> int:
        parent_num = 0
        max_parent_num = 0
        kavicki = 0
        for i in range(len(s)):
            if s[i] == "\"" and kavicki % 2 == 0:
                kavicki += 1
                parent_num += 1
                if parent_num > max_parent_num:
                    max_parent_num = parent_num
            elif s[i] == "(":
                parent_num += 1
                if parent_num > max_parent_num:
                    max_parent_num = parent_num
            elif s[i] == "\"" and kavicki % 2 != 0:
                kavicki -= 1
                parent_num -= 1
            elif s[i] == ")":
                parent_num -= 1
        return max_parent_num
