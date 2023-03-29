stones = {}
command = input()
while command != "stop":
    if command not in stones.keys():
        stones[command] = int(input())
    else:
        stones[command] += int(input())
    command = input()
for stone, qty in stones.items():
    print(f"{stone} -> {qty}")
