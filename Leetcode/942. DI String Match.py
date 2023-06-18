class Solution:
    def diStringMatch(self, s: str):
        perm=[]
        min_num=0
        max_num=len(s)
        for i in s:
            if i=='I':
                perm.append(min_num)
                min_num += 1
            else:
                perm.append(max_num)
                max_num -= 1
        if s[len(s)-1]=='I':
            perm.append(max_num)
        else:
            perm.append(min_num)
        return perm
