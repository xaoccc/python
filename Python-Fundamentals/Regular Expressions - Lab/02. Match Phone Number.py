
import re
text_input = input()
# () is used for grouping of patterns, we see that the whole pattern is in () and the boundary(\b) is outside. If we need this pattern elsewhere, we can call it by writing \1 later in the pattern, outside this group, as this is the first group
# inside the group we check for valid phone number:
# \+ we escape the "+" character, because it is a system character
# +359 - we need this exact pattern, then we have either " " or "-", so we make a group with both of them ([\s\-]) \s for white space and \- for dash. Later in the pattern, we use \2 to get the same input as the one used the first time, so we can have +359 2 222 2222, but +359 2-222 2222 is not allowed, because we need to have the same digits separator.
# 2 is the exact digit 2
# d{3} means 3 digits from 0 to 9 incl.
# d{4} means 4 digits from 0 to 9 incl.

pattern = r'(\+359([\s\-])2\2\d{3}\2\d{4})\b'
result = re.findall(pattern, text_input)

# Very important! When we have capture inside the capture, the output is tuples inside a list, so here we have to get the info from the tuples 
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i][0])
    else:
        print(result[i][0], end=", ")

# This is the standard solution of this problem, using 2 different patterns - with space and with dash        
# import re
# text_input = input()
# pattern = r'(\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4})\b'
# result = re.findall(pattern, text_input)
# print(", ".join(result))
