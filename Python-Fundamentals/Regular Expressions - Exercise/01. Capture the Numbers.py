import re
output = []
while True:
    command = input()
    if command:
        output += re.findall(r'\d+', command)
    else:
        break

print(" ".join(output))
