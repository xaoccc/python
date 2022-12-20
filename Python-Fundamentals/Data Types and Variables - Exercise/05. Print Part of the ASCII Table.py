ascii_start = int(input())
ascii_end = int(input())
for ord in range(ascii_start, ascii_end + 1):
  print(chr(ord), end=" ")
