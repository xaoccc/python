import re
main_string = input().lower()
pattern = input().lower()
scanner = re.findall(pattern, main_string)
print(len(scanner))


import re
import string
main_string = input().lower().translate(str.maketrans("", "", string.punctuation)).split()
pattern = input().lower()
print(main_string.count(pattern))

import re
main_string = input().lower()
pattern = input().lower()
res = re.sub(r'[^\w\s]', ' ', main_string).split()
print(res.count(pattern))
