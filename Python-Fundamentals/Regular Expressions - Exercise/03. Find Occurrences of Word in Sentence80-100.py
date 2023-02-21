import re
main_string = input().lower()
pattern = input().lower()
scanner = re.findall(pattern, main_string)
print(len(scanner))
