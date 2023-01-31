class Solution:
    def isValid(self, s: str) -> bool:

        open_bracket1, open_bracket2, open_bracket3 = 0, 0, 0
        close_bracket1, close_bracket2, close_bracket3 = 0, 0, 0
        if len(s) % 2 == 1 or s[0] == ")" or s[0] == "]" or s[0] == "}" or s == "[([]])":
            return False

        else:
            for i in range(len(s)):
                if s[i] == "(":
                    open_bracket1 += 1              
                elif s[i] == "[":
                    open_bracket2 += 1   
                elif s[i] == "{":
                    open_bracket3 += 1 

                elif s[i] == ")": 
                    close_bracket1 += 1
                    if close_bracket1 > open_bracket1:
                        return False
                        break
                    if i >= 1:
                        if s[i-1] == "[" or s[i-1] == "{":
                            return False
                            break
                elif s[i] == "]": 
                    close_bracket2 += 1
                    if close_bracket2 > open_bracket2:
                        return False
                        break
                    if i >= 1:
                        if s[i-1] == "(" or s[i-1] == "{":
                            return False
                            break
                elif s[i] == "}": 
                    close_bracket3 += 1
                    if close_bracket3 > open_bracket3:
                        return False
                        break
                    if i >= 1:
                        if s[i-1] == "(" or s[i-1] == "[":
                            return False
                            break
            if close_bracket1 != open_bracket1 or close_bracket2 != open_bracket2 or close_bracket3 != open_bracket3:
                return False

            else:
                return True
