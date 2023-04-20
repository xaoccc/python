from collections import deque
import operator
bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
process = deque(map(str, input().split()))
total_nectar = 0

while bees and nectar and process:
    if bees[0] <= nectar[-1]:
        if (nectar[-1] == 0 or bees[0] == 0) and process[0] == "/":
            process.popleft()
            nectar.pop()
            bees.popleft()
            continue

        op_func = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }.get(process.popleft())
        total_nectar += abs(op_func(bees.popleft(), nectar[-1]))
    nectar.pop()

print(f"Total honey made: {total_nectar}")
if bees:
    print(f"Bees left: {', '.join([str(i) for i in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(i) for i in nectar])}")
