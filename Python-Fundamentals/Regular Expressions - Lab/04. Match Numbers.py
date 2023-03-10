import re
num = input()
# (^|(?<=\s)) - means if there is nothing before the string or there is a whitespace: ?<= lookbehind for a whitespace \s
# -? - means there might be one dash or not
# ([0]|[1-9][0-9]*) - the number is [0] OR it begins with [1-9] and after that the digits are [0-9] zero or more times: *
# (\.\d+)? - then we might have or might not have dot AND digits after it, because they are grouped, we cannot have just dot or just digits, because we have question mark, this group may occur zero or one time, but not more than once
# ($|(?=\s)) - the look forward statement says we can end with white space or just end the string

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'

results = re.finditer(pattern, num)
for result in results:
    print(result.group(), end=" ")
