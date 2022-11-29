num = int(input())
current = 1
is_bigger_than_num = False

for row in range(1, num + 1):
    for col in range(1, row + 1):
        if num < current:
            is_bigger_than_num = True
            break
        print(str(current)+ " ", end = "")
        current += 1
    if is_bigger_than_num:
        break
    print()