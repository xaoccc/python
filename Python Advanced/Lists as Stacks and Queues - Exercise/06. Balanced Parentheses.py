s = input()
open_par = ["(", "[", "{"]
close_par = [")", "]", "}"]
used = []
if s[0] not in open_par or len(s) % 2 != 0:
    print("NO")
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
        print("NO")
    elif len(used) == 0 and i == len(s) -1:
        print("YES")



# s = input()
# open_bracket1, open_bracket2, open_bracket3 = 0, 0, 0
# close_bracket1, close_bracket2, close_bracket3 = 0, 0, 0
# if len(s) % 2 == 1 or s[0] == ")" or s[0] == "]" or s[0] == "}" or s == "[([]])":
#     print("NO")

# else:
#     for i in range(len(s)):
#         if s[i] == "(":
#             open_bracket1 += 1              
#         elif s[i] == "[":
#             open_bracket2 += 1   
#         elif s[i] == "{":
#             open_bracket3 += 1 

#         elif s[i] == ")": 
#             close_bracket1 += 1
#             if close_bracket1 > open_bracket1:
#                 break
#             if i >= 1:
#                 if s[i-1] == "[" or s[i-1] == "{":
#                     break
#         elif s[i] == "]": 
#             close_bracket2 += 1
#             if close_bracket2 > open_bracket2:
#                 break
#             if i >= 1:
#                 if s[i-1] == "(" or s[i-1] == "{":
#                     break
#         elif s[i] == "}": 
#             close_bracket3 += 1
#             if close_bracket3 > open_bracket3:
#                 break
#             if i >= 1:
#                 if s[i-1] == "(" or s[i-1] == "[":
#                     break
#     if close_bracket1 != open_bracket1 or close_bracket2 != open_bracket2 or close_bracket3 != open_bracket3:
#         print("NO")

#     else:
#         print("YES")
