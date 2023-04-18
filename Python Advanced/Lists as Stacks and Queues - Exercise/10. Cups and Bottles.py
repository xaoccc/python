from collections import deque

cups = deque(int(i) for i in input().split())
bottles = deque(int(i) for i in input().split())
wasted_water = 0

while cups:
    if cups[0] > bottles[-1]:
        cups[0] -= bottles[-1]
        bottles.pop()
    elif cups[0] <= bottles[-1]:
        wasted_water += bottles[-1] - cups[0]
        cups.popleft()
        bottles.pop()
    if not bottles or not cups:
        break
if not bottles:
    print(f"Cups: {' '.join([str(i) for i in cups])}")
elif bottles and not cups:        
    print(f"Bottles: {' '.join([str(i) for i in bottles])}")

print(f"Wasted litters of water: {wasted_water}")
