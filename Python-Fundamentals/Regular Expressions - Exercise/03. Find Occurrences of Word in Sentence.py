import re
main_string = input().lower()
check_string = input().lower()
pattern = r'(^|(?<=[\W\_]))' + re.escape(check_string) + r'($|(?=[\W\_]))'
res = re.findall(pattern, main_string)
print(len(res))


# import re
# main_string = input().lower()
# check_string = input().lower()
# matches = re.findall(rf"\b{check_string}\b", main_string)
# print(len(matches))
