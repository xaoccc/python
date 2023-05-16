class Solution:
    def isValid(self, s: str) -> bool:
        open_par = ["(", "[", "{"]
        close_par = [")", "]", "}"]
        used = []
        if s[0] not in open_par or len(s) % 2 != 0:
            return False
        else:
            for i in range(len(s)):
                if s[i] in open_par:
                    used.append(s[i])
                elif len(used) == 0:
                    print("NO")
                    break
                else:
                    if used[-1] == open_par[close_par.index(s[i])]:
                        used.pop()
                    else:
                        break
            if len(used) > 0:
                return False
            elif len(used) == 0 and i == len(s) -1:
                return True
