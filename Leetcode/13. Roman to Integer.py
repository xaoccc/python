class Solution(object):
    def romanToInt(self, s):
        num = 0
        
        for i in range(len(s)):
            if s[i] == "I":
                num += 1
            elif s[i] == "V":
                if i > 0 and s[i - 1] == "I":
                    num += 3
                else:
                    num += 5
            elif s[i] == "X":
                if i > 0 and s[i - 1] == "I":
                    num += 8
                else:
                    num += 10
            elif s[i] == "L":
                if i > 0 and s[i - 1] == "X":
                    num += 30
                else:
                    num += 50
            elif s[i] == "C":
                if i > 0 and s[i - 1] == "X":
                    num += 80
                else:
                    num += 100
            elif s[i] == "D":
                if i > 0 and s[i - 1] == "C":
                    num += 300
                else:
                    num += 500
            elif s[i] == "M":
                if i > 0 and s[i - 1] == "C":
                    num += 800
                else:
                    num += 1000                
        return num
