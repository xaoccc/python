
import re
text_input = input().split()
scanner = ""
for i in text_input:
    scanner += ",".join(re.findall(r"^_[a-zA-Z0-9]+\b", i))
scanner = scanner.split("_")
del scanner[0]
print(",".join(scanner))


