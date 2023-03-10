import re

text_input = input().split()
pattern = re.compile('(^|(?<=\s))[A-Za-z]+([\.\-\_][A-Za-z]+)*@[A-Za-z]+(\-[A-Za-z]+)*([\.{1}][A-Za-z]+(\-[A-Za-z]+)*)+($|(?=[\s\W]))')

for i in text_input:
    for match in re.finditer(pattern, i):
        print(match.group().rstrip("."))
        
# (^|(?<=\s)) - checks for beginning with space or nothing (email is in the beginning of string)
# [A-Za-z]+  - the email must start with at least one alphabetical character
# ([\.\-\_][A-Za-z]+)*   - after this character(s) we can have 1 of the following: ".", "-" or "_" and at lest one character. We can repeat this pattern from zero to unlimited times
# @  - then we have @
# [A-Za-z]+   - again we must start with at least one alphabetical character
# (\-[A-Za-z]+)* - we can have "-" inside the text, but maybe not, that is why we write "*"
# ([\.{1}][A-Za-z]+(\-[A-Za-z]+)*)+  - the pattern "." + some text [A-Za-z]+ maybe with dash in it (\-[A-Za-z]+)* must repeat at least once for domain name to be valid
# ($|(?=[\s\W]))  - a valid end of an email can be a no-alphabetic character "\W", white space "\s" or end of string.

