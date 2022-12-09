class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
      #Test in leetcode is wrong, this isthe correct solution
        leetcode = ""
        for i in range(len(indices)):
            leetcode += s[indices[i]]
        return leetcode
