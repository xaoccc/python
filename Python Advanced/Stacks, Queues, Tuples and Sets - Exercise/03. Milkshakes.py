from collections import deque
choco = [int(i) for i in input().split(", ")]
milk = deque([int(i) for i in input().split(", ")])
milkshakes = 0
i = len(choco) - 1

while True:
    if milk[0] <= 0:
        milk.popleft()
    if choco[i] <= 0:
        choco.pop(i)
        i -= 1
    if i == -1:
        i = len(choco) - 1
    if not choco or not milk:
        break
    if choco[i] == milk[0]:
        milkshakes += 1
        milk.popleft()
        choco.pop(i)
    else:
        milk.append(milk.popleft())
        choco[i] -= 5
    i -= 1
    if not choco or not milk or milkshakes == 5:
        break
    if i == -1:
        i = len(choco) - 1

if milkshakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")
    
if choco:
    print(f"Chocolate: {', '.join([str(i) for i in choco])}")
else:
    print("Chocolate: empty")
    
if milk:
    print(f"Milk: {', '.join([str(i) for i in milk])}")
else:
    print("Milk: empty")
