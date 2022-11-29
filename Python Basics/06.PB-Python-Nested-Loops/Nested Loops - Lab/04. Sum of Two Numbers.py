num1 = int(input())
num2 = int(input())
magic_num = int(input())
combination_count = 0
combination_ok = ""

for n1 in range(num1, num2 + 1 ):
    for n2 in range(num1, num2 + 1):
        combination_count += 1
        if combination_ok == "ok":
            continue
        if (n1 + n2) == magic_num:
            print(f"Combination N:{combination_count} ({n1} + {n2} = {magic_num})")
            combination_ok = "ok"
            break
        else:
            combination_ok = "nok"
if combination_ok == "nok":
    print(f"{combination_count} combinations - neither equals {magic_num}")