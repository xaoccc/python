rows, cols = [int(i) for i in input().split()]

for row in range(rows):
    for col in range(cols):
        print(chr(97 + row)+chr(97 + row + col)+chr(97 + row), end=" ")
    print()
