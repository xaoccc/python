import re

text_input = input().split()
pattern = re.compile(r'^([A-Za-z0-9])+([\.\-\_][A-Za-z0-9]+)*@([A-Za-z-]+)\.([A-Za-z-]+)([\.A-Za-z-])*[\.A-Za-z]$')

for i in text_input:
    for match in re.finditer(pattern, i):
        print(match.group().rstrip("."))
        
#test 2 judge - testing for emails edning in "."
#No emails are ending with "-"
