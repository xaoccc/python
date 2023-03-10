import re

text_input = input().split()
pattern = re.compile('(^|(?<=\s))([A-Za-z]+[\.\-\_]*[A-Za-z]+)@[A-Za-z]+(\-[A-Za-z]+)*([\.{1}][A-Za-z]+(\-[A-Za-z]+)*)+($|(?=[\s\W]))')

for i in text_input:
    for match in re.finditer(pattern, i):
        print(match.group().rstrip("."))
        
#test 2 judge - testing for emails edning in "."
#No emails are ending with "-"
