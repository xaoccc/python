import re
main_string = input().lower()
check_string = input().lower()
pattern = r'(^|(?<=[\W\_]))' + re.escape(check_string) + r'($|(?=[\W\_]))'
res = re.findall(pattern, main_string)
print(len(res))
