chars = input().split(", ")
ascii_data = {}
for i in chars:
    ascii_data[i] = ord(i)
print(ascii_data)
