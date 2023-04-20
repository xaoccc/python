from collections import deque
import operator
bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
process = deque(map(str, input().split()))
total_nectar = 0

while bees and nectar and process:
    if bees[0] <= nectar[-1]:
        op_func = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "%": operator.mod,
        }.get(process[0])
        total_nectar += abs(op_func(bees[0], nectar[-1]))
        bees.popleft()
        nectar.pop()
        process.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {total_nectar}")
if bees:
    print(f"Bees left: {', '.join([str(i) for i in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(i) for i in nectar])}")
