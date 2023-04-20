from collections import deque
choco = [int(i) for i in input().split(", ")]
milk = deque([int(i) for i in input().split(", ")])
milkshakes = 0

while choco and milk and milkshakes < 5:
    flag = False
    if milk[0] <= 0:
        milk.popleft()
        flag = True
    if choco[-1] <= 0:
        choco.pop()
        flag = True
    if flag:
        continue
    if choco[-1] == milk[0]:
        milkshakes += 1
        milk.popleft()
        choco.pop()
    else:
        milk.append(milk.popleft())
        choco[-1] -= 5

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
